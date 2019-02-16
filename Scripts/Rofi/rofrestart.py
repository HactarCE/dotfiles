#!/usr/bin/env python3

KILL_LIMIT = 4
KILL_WAIT = 0.1

from subprocess import call, check_output
from time import sleep
from utils import rofi, subtext

PROGRAMS = '''\
compton
discord
dropbox
dunst
nemo
pulseaudio
redshift
steam
'''.splitlines()

def check(progname):
    """Checks whether a program is running using pgrep. Return True if the program was found."""
    print("Checking for", progname)
    return not call(['pgrep', '-xi', progname])

def kill(progname):
    """Attempt to kill the program using pkill. Returns True if the program was found."""
    print("Killing", progname)
    return not call(['pkill', '-xi', progname])

options = [s.capitalize() for s in PROGRAMS]
for i in range(len(options)):
    if not check(PROGRAMS[i]):
        options[i] += subtext("not running")

progname = PROGRAMS[rofi(options, '-markup-rows', p='Toggle', format='i')]

if check(progname):
    print("Found", progname)
    while KILL_LIMIT > 0 and kill(progname):
        KILL_LIMIT -= 1
        sleep(KILL_WAIT)
else:
    print("Did not find", progname)
    print("Starting", progname)
    call(['i3', f'exec --no-startup-id {progname}'])
