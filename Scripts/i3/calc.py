#!/bin/env python3

CALC_COMMAND = 'exec speedcrunch'
CALC_CLASS = 'SpeedCrunch' # the second one from xprop WM_CLASS
CALC_CRITERIA = f'[class="{CALC_CLASS}"]'

from subprocess import call, CalledProcessError
import utils

# Try to unfocus calculator if it is active
try:
    if utils.get_win_prop('wm_class') == CALC_CLASS:
        # window is active
        utils.i3.command('focus mode_toggle') # works as long as calculator is a floating window
        exit()
except CalledProcessError:
    pass

# Try to focus calculator if it exists
try:
    if not call(['xdotool', 'search', '--class', CALC_CLASS]):
        utils.i3.command(CALC_CRITERIA + ' focus')
except CalledProcessError:
    pass

# Try to execute calculator
else:
    utils.i3_exec(CALC_COMMAND)
