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

with utils.MultiPressChecker(TEMPFILE) as multipress:
    if not multipress.first:
        exit()
    is_running = not call(XDOTOOL_SEARCH_COMMAND)
    if not is_running:
        if multipress.wait(2):
            # If not running, start the program on double-press
            # i3_exec is not portable to other WMs/DEs :(
            utils.i3_exec(CALC_COMMAND)
    else:
        win_id = check_output(XDOTOOL_SEARCH_COMMAND).splitlines()[0]
        # Window exists
        if not utils.win_is_mapped(win_id):
            # If not mapped, map it
            utils.win_map(win_id)
        else:
            # Window is mapped
            if not utils.win_is_visible(win_id):
                # If not visible, focus it
                utils.win_focus(win_id)
            else:
                # Window is visible
                if not utils.win_is_active(win_id):
                    # If not active, focus it
                    utils.win_focus(win_id)
                    if multipress.wait(2):
                        # If double-pressed when visible but inactive, unmap it
                        utils.win_unmap(win_id)
                else:
                    # Window is active
                    # If pressed when active, unmap it
                    utils.win_unmap(win_id)
                    if multipress.wait(2):
                        # If double-pressed when active, close it
                        utils.win_close(win_id)
