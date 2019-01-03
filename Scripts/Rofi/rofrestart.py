#!/usr/bin/env python3

from subprocess import call, check_output
from utils import rofi, subtext

PROGRAMS = '''\
compton
dropbox
dunst
pulseaudio
redshift
'''.splitlines()

options = [s.capitalize() for s in PROGRAMS]
for i in range(len(options)):
    if call(['pgrep', '-x', PROGRAMS[i]]):
        options[i] += subtext("not running")

progname = PROGRAMS[rofi(options, '-markup-rows', p='Toggle', format='i')]

if call(['pkill', '-x', progname]):
    call(['i3', f'exec --no-startup-id {progname}'])

def autorandr(*args, **kwargs):
    return check_output(['autorandr', '--skip-options', 'gamma'] + list(args), **kwargs).decode()

def subtext(s):
    return f' <span weight="light"><i><small>({s})</small></i></span>'
