#!/bin/env python3

CALC_CLASS = 'speedcrunch'
CALC_COMMAND = 'exec speedcrunch'

from subprocess import call
import utils

if utils.get_win_prop('wm_class') == CALC_CLASS:
    # window is active
    utils.i3.command('focus mode_toggle') # works as long as calculator is a floating window
elif not call(['xdotool', 'search', '--class', CALC_CLASS]):
    # window exists
    utils.i3.command('[class="SpeedCrunch"] focus')
else:
    # window does not exist
    utils.i3_exec(CALC_COMMAND)
