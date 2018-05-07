#!/usr/bin/env python3

import os
import subprocess
from time import sleep

def sh_no_block(cmd, *args, **kwargs):
    if isinstance(cmd, str):
        cmd = cmd.split()
    return subprocess.Popen(cmd, *args, **kwargs)

def sh(cmd, *args, **kwargs):
    return sh_no_block(cmd, *args, stdout=subprocess.PIPE, **kwargs).communicate()[0]

# Terminate already running bar instances
sh('killall -q polybar')

# Wait until the processes have been shut down
while sh('pgrep -u {} -x polybar'.format(os.getuid())):
    sleep(0.2)

# Launch bars
print(sh('printenv', env={'evtest': 'potato', 'test1': 'test2'}).decode('ascii'))
try:
    xrandr = [line.decode('ascii').split() for line in sh('xrandr').splitlines()]
    for line in xrandr:
        if 'connected' in line:
            print('Launching bar on ' + line[0] + (' (primary)' if 'primary' in line else ''))
            env = os.environ.copy()
            env['MONITOR'] = line[0]
            env['TRAY_POS'] = 'right' if 'primary' in line else ''
            # sh_no_block('polybar bottom')
            sh_no_block('polybar bottom', env=env)
            sh_no_block('polybar top', env=env)
except Exception as e:
    print(e)
    print('Launching bar')
    env = os.environ.copy()
    env['TRAY_POS'] = 'right'
    sh_no_block('polybar bottom', env=env)
    sh_no_block('polybar top', env=env)

print('Done')
