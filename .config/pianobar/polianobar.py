#!/usr/bin/env python3

###############################################################################
### BEGIN CONFIGURATION SECTION
###############################################################################

# Configure whatever you want in here (just don't break things).

PIANOBAR_COMMAND = 'pianobar'

# If you change this, be sure to change the same setting in eventcmd.py,
# control.sh, and getstatus.sh.
STATUS_FILE = '~/.config/pianobar/status'

# Make sure that this file is NOT specified in Pianobar's config file. If you
# change it, be sure to change the same setting in control.sh.
PIANOBAR_FIFO_FILE = '~/.config/pianobar/ctl'

# This is for use with eventcmd. If you change it, be sure to change the same
# setting in eventcmd.py and control.sh.
EVENTCMD_FIFO_FILE = '~/.config/pianobar/eventcmd_fifo'

LYRICS_FILE = '~/.config/pianobar/lyrics'

CONTROL_SH = '~/.config/pianobar/control.sh'

MAX_SONG_NAME_LENGTH = 130

# If you've changed any of Pianobar's keybinds, update them in control.sh.

def get_status():
    if info['isPlaying']:
        playpause_action = 'play' if info['isPlaying'] == 'pause' else 'pause'
        s = ''
        # Play/pause/skip/stop buttons
        s += button('栗', control_action('quit')) + ' '
        s += button('契'[info['isPlaying'] == 'pause'], control_action(playpause_action)) + ' '
        s += button('怜', control_action('skip')) + '  '
        # Bar
        barLength = 30
        timePlayed, timeTotal = info['timePlayed'], info['timeTotal']
        s += f'{timePlayed//60:02}:{timePlayed%60:02} '
        s += f'%{{A1:{control_action(playpause_action)}:}}'
        progress = int(timePlayed / timeTotal * barLength)
        s += f'%{{F#99}}'
        s += '▒' * progress
        if info['buffering']:
            s += f'%{{F#333333}}'
        else:
            s += f'%{{F#cccccc}}%{{T3}}█%{{T-}}%{{F#555555}}'
        s += '▒' * (barLength - progress - (not info['buffering']))
        s += f'%{{F-}}'
        s += f'%{{A}}'
        s += f' {timeTotal//60:02}:{timeTotal%60:02}  '
        # Love/ban/shelf buttons
        s += button('﨑塚'[info['rating'] == '2'], control_action('ban')) + ' '
        s += button('鈴', control_action('shelf')) + ' '
        s += button('﨓晴'[info['rating'] == '1'], control_action('love')) + '  '
        # Title/album/artist
        s += format_songname(True, True, MAX_SONG_NAME_LENGTH)
        # Lyrics
        if lyrics_text:
            s += ' ' + button('%{F#cccccc}(lyrics)%{F-}', f'mousepad {LYRICS_FILE}')
        return s
    return format_stationname()

def transient_message(event):
    global transient_text, transient_time
    # Possible values for event:
    # 'songlove', 'songban', 'songshelf', 'stationfetchplaylist', 'userlogin'
    if event in ('songlove', 'songban', 'songshelf'):
        transient_text = {
            'songlove': f"Loving {format_songname(True, False)}...",
            'songban': f"Banning {format_songname(True, False)}...",
            'songshelf': f"Shelving {format_songname(True, False)}..."
        }[event]
        transient_time = 2
    elif event == 'stationfetchplaylist':
        transient_text = f"Fetching playlist on {format_stationname()}..."
        transient_time = 1
    elif event == 'userlogin':
        transient_text = "Sign-in successful."
        transient_time = 0.5

def toggle_action():
    global transient_text, transient_time
    s = ''
    s += "Currently playing station "
    s += format_stationname()
    transient_text = s
    transient_time = 2

# This method is only used in the configuration section -- feel free to modify
# or remove it.
def button(icon, action):
    # return f'%{{A1:{action}:}}%{{F#0070da}}{icon}%{{F-}}%{{A}}'
    # return f'%{{A1:{action}:}}%{{F#80B8ED}}{icon}%{{F-}}%{{A}}'
    # return f'%{{A1:{action}:}}%{{F#99ccff}}{icon}%{{F-}}%{{A}}'
    return f'%{{A1:{action}:}}%{{F#ff99ff}}{icon}%{{F-}}%{{A}}'
    # return f'%{{A1:{action}:}}{icon}%{{A}}'

def control_action(arg):
    return f'{CONTROL_SH} {arg}'

# This method is only used in the configuration section -- feel free to modify
# or remove it.
def format_songname(show_artist=False, show_album=False, max_length=None):
    title, artist, album = info['title'], info['artist'], info['album']
    if max_length:
        if show_artist:
            if len(f"{title} by {artist} on {album}") > max_length:
                show_album = False
            if len(f"{title} by {artist}") > max_length:
                show_artist = False
        elif len(f"{title} on {album}") > max_length:
            show_album = False
        if len(title) > max_length:
            title = title[:max_length-3] + '...'
    s = f'%{{F#66cc66}}{title}%{{F-}}'
    if show_artist:
        s += f' by %{{F#00ccff}}{artist}%{{F-}}'
    if show_album:
        s += f' on %{{F#cccc00}}{album}%{{F-}}'
    return s

# This method is only used in the configuration section -- feel free to modify
# or remove it.
def format_stationname():
    return f'%{{F#cc6699}}{info["stationName"]}%{{F-}}'

###############################################################################
### END CONFIGURATION SECTION
###############################################################################

from utils import timeout
import atexit
import errno
import fcntl
import io
import os
import re
import select
import signal
import subprocess
import sys
import termios
import time
import tty

try:
    import tswift
    GET_LYRICS = True
except:
    GET_LYRICS = False

STATUS_FILE = os.path.expanduser(STATUS_FILE)
PIANOBAR_FIFO_FILE = os.path.expanduser(PIANOBAR_FIFO_FILE)
EVENTCMD_FIFO_FILE = os.path.expanduser(EVENTCMD_FIFO_FILE)
LYRICS_FILE = os.path.expanduser(LYRICS_FILE)
CONTROL_SH = os.path.expanduser(CONTROL_SH)

info = {'isPlaying': False, 'buffering': True}
transient_text = None
transient_time = None
lyrics_text = None

#region Setup

# Set up general Pianobar FIFO file for reading.
if not os.path.exists(PIANOBAR_FIFO_FILE):
    os.mkfifo(PIANOBAR_FIFO_FILE, 0o666)
pianobar_fifo = os.open(PIANOBAR_FIFO_FILE, os.O_RDONLY | os.O_NONBLOCK)

# Set up Polianobar eventcmd FIFO file for reading
if not os.path.exists(EVENTCMD_FIFO_FILE):
    os.mkfifo(EVENTCMD_FIFO_FILE, 0o666)
eventcmd_fifo = os.open(EVENTCMD_FIFO_FILE, os.O_RDONLY | os.O_NONBLOCK)

old_terminal_settings = termios.tcgetattr(sys.stdin)

pianobar = subprocess.Popen(PIANOBAR_COMMAND.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE)

def signal_handler(sig, frame):
    pianobar.send_signal(sig)
    # TODO BUG stdout doesn't update
signal.signal(signal.SIGINT, signal_handler)

def set_status(text):
    with open(STATUS_FILE, 'w') as f:
        f.write(text)
        if not text.endswith('\n'):
            f.write('\n')

@atexit.register
def rm_status():
    pianobar.terminate()
    if os.path.isfile(STATUS_FILE):
        os.remove(STATUS_FILE)
    # Fix terminal
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_terminal_settings)

#endregion

#region Non-blocking I/O

# Set non-blocking reading of Pianobar's stdout.
pianobar_fd = pianobar.stdout.fileno()
fcntl.fcntl(pianobar_fd, fcntl.F_SETFL, fcntl.fcntl(pianobar_fd, fcntl.F_GETFL) | os.O_NONBLOCK)

# Set non-blocking reading of stdin (from terminal).
tty.setcbreak(sys.stdin.fileno())

def read_stdin():
    s = ''
    while select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
        s += sys.stdin.read(1)
    return s

def read_pianobar_stdout():
    try:
        return pianobar.stdout.read().decode('UTF-8')
    except: return ''

def read_fifo(fifo):
    s = ''
    buffer = True
    while buffer:
        try:
            buffer = os.read(fifo, io.DEFAULT_BUFFER_SIZE).decode('UTF-8')
            s += buffer
        except OSError as err:
            if err.errno == errno.EAGAIN or err.errno == errno.EWOULDBLOCK:
                buffer = None
            else:
                raise
    return s

def remove_parens(s):
    return re.sub(r'\([^)]*\)', '', s).strip()

#endregion

#region Update handlers

def parse_min_sec(s):
    split = s.split(':')
    return int(split[0]) * 60 + int(split[1])

def update_status():
    set_status(get_status())

def handle_eventcmd(type, new_info):
    global lyrics_text
    info.update(new_info)
    info['timePlayed'] = int(info['songPlayed'])
    info['timeTotal'] = int(info['songDuration'])
    info['timeRemaining'] = info['timeTotal'] - info['timePlayed']
    if type == 'songstart':
        info['isPlaying'] = 'play'
        info['buffering'] = True
        if GET_LYRICS:
            try:
                lyrics_text = tswift.Song(remove_parens(info['title']),
                                          remove_parens(info['artist'])).lyrics
            except:
                lyrics_text = None
        with open(LYRICS_FILE, 'w') as f:
            if lyrics_text:
                f.write(lyrics_text)
        update_status()
    elif type in ('songlove', 'songban', 'songshelf', 'stationfetchplaylist', 'userlogin'):
        transient_message(type)
        if type == 'songfinish':
            info['isPlaying'] = False
            update_status()
    elif type == 'toggle':
        toggle_action()

def handle_stdin(char):
    if info['isPlaying'] and char in 'p PS':
        if char in 'p ':
            if info['isPlaying'] == 'pause':
                info['isPlaying'] = 'play'
            else:
                info['isPlaying'] = 'pause'
        elif char == 'P':
            info['isPlaying'] = 'play'
        elif char == 'S':
            info['isPlaying'] = 'pause'
        update_status()

def handle_time_update(remaining_string, total_string) :
    info['timeRemaining'] = parse_min_sec(remaining_string)
    info['timeTotal'] = parse_min_sec(total_string)
    info['timePlayed'] = info['timeTotal'] - info['timeRemaining']
    info['buffering'] = False
    update_status()

#endregion

time_pattern = re.compile(r'#\s+-(\d+:\d+)/(\d+:\d+)')

last_line = ''
while pianobar.poll() is None:
    time.sleep(0.1)
    #region transient_text
    if transient_text:
        set_status(transient_text)
        time.sleep(transient_time)
        transient_text = None
        transient_time = None
    #endregion
    #region eventcmd
    eventcmd_buffer = read_fifo(eventcmd_fifo)
    if eventcmd_buffer:
        try:
            with timeout(seconds=1):
                while not eventcmd_buffer.strip().endswith('\n~~~'):
                    eventcmd_buffer += read_fifo(eventcmd_fifo)
                for eventcmd in eventcmd_buffer.split('\n~~~'):
                    eventcmd = eventcmd.strip()
                    if eventcmd:
                        lines = eventcmd.splitlines()
                        new_info = {}
                        for line in lines[1:]:
                            key, _, value = line.partition('=')
                            new_info[key] = value
                        handle_eventcmd(lines[0], new_info)
        except TimeoutError:
            print("Timeout error searching for endof:", repr(eventcmd_buffer))
    #endregion
    #region stdin
    stdin_buffer = ''
    try:
        with timeout(seconds=1):
            stdin_buffer = read_stdin() + read_fifo(pianobar_fifo)
            if stdin_buffer:
                pianobar.stdin.write(stdin_buffer.encode('UTF-8'))
                pianobar.stdin.flush()
                for char in stdin_buffer:
                    handle_stdin(char)
    except TimeoutError:
        print("Timeout error while handling input:", repr(stdin_buffer))
    #endregion
    #region stdout
    stdout_buffer = ''
    try:
        with timeout(seconds=1):
            stdout_buffer = read_pianobar_stdout()
            if stdout_buffer:
                sys.stdout.write(stdout_buffer)
                sys.stdout.flush()
                last_line = (last_line + stdout_buffer).split('\x1b[2K')[-1]
                m = time_pattern.match(last_line)
                if m:
                    handle_time_update(*m.groups())
    except TimeoutError:
        print("Timeout error while handling output:", repr(stdout_buffer))
    #endregion
