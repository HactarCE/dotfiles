#!/usr/bin/env python3

import os
import utils

i3exit = os.path.join(utils.script_dir, 'i3exit.sh')

menu = ['lock', 'logout', 'suspend', 'hibernate', 'reboot', 'shutdown']

choice = utils.dmenu(menu, prompt='i3exit')
if choice:
    utils.i3_exec_nsi(i3exit + ' ' + choice)
