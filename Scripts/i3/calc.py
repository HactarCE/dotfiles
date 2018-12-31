#!/bin/env python3

# DEPENDENCIES:
# - xdotool
# - xwininfo

CALC_CLASS = 'speedcrunch'
CALC_COMMAND = 'exec speedcrunch'
DOUBLEPRESS_TIMEOUT = 0.25

XDOTOOL_SEARCH_COMMAND = ['xdotool', 'search', '--class', CALC_CLASS]

TEMPFILENAME = '.calc_doublepress'

from os import path
from sys import argv
from subprocess import call, check_output, TimeoutExpired
import os
import utils

TEMPFILE = path.join(path.dirname(path.abspath(__file__)), TEMPFILENAME)
print(TEMPFILE)

def await_doublepress(timeout=0.25):
    try:
        with open(TEMPFILE, 'r+') as f:
            presses = int(f.read())
            f.seek(0)
            f.write(str(presses + 1))
            exit()
    except:
        with open(TEMPFILE, 'w') as f:
            presses = 1
            f.write("1")
    try:
        call(['inotifywait', '-e', 'modify', TEMPFILE], timeout=DOUBLEPRESS_TIMEOUT)
        return True
    except TimeoutExpired:
        return False
    finally:
        os.remove(TEMPFILE)

is_running = not call(XDOTOOL_SEARCH_COMMAND)
if is_running:
    win_id = check_output(XDOTOOL_SEARCH_COMMAND).splitlines()[0]
    print('hi')
    print(win_id)
    if utils.win_is_mapped(win_id):
        print('map')
        if utils.win_is_visible(win_id):
            print('vis')
            if utils.win_is_active(win_id):
                print('act')
                if await_doublepress():
                    print('double!')
                    # If double-pressed when active, close it
                    utils.win_close(win_id)
                else:
                    # If single-pressed when active, unmap it
                    utils.win_unmap(win_id)
            else:
                # If not active, focus it
                utils.win_focus(win_id)
        else:
            # If not visible, focus it
            utils.win_focus(win_id)
    else:
        # If not mapped, map it
        utils.win_map(win_id)
elif await_doublepress():
    # If not running, start the program on double-press
    # i3_exec is not portable to other WMs/DEs :(
    utils.i3_exec(CALC_COMMAND)
