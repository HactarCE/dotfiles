#!/usr/bin/env python3

from subprocess import call
from time import sleep
from utils import rofi, subtext


KILL_LIMIT = 4
KILL_WAIT = 0.1

PROGRAMS = '''\
discord
dropbox
dunst
Libinput Gestures %% libinput-gestures
nemo
pCloud %% /home/andrew/Scripts/Polybar/run-pcloud.sh
picom
pulseaudio
redshift
steam
OneDrive %% onedrive --monitor
timidity %% timidity -iA
'''.splitlines()


def check(progname):
    """Checks whether a program is running using pgrep. Return True if the program was found."""
    print("Checking for", progname)
    return not call(['pgrep', '-xi', progname])


def kill(progname):
    """Attempt to kill the program using pkill. Returns True if the program was found."""
    print("Killing", progname)
    return not call(['pkill', '-SIGTERM', '-xi', progname])


commands = [s.split('%%')[-1].strip() for s in PROGRAMS]
prognames = [s.split('%%')[0].strip() for s in PROGRAMS]
options = [s.capitalize() if s.islower() else s for s in prognames]
for i in range(len(options)):
    if not check(prognames[i]):
        options[i] += subtext("not running")

i = rofi(options, '-markup-rows', p='Toggle', format='i')
progname = prognames[i]

if check(progname):
    print("Found", progname)
    while KILL_LIMIT > 0 and kill(progname):
        KILL_LIMIT -= 1
        sleep(KILL_WAIT)
else:
    print("Did not find", progname)
    print("Starting", progname)
    call(['i3', f'exec --no-startup-id {commands[i]}'])
