#!/usr/bin/env python3

import os
import subprocess
from time import sleep

PID_FILE_FMT = os.path.join('/var/run/user', str(os.getuid()), 'polybar-{}.pid')

def sh_no_block(cmd, *args, **kwargs):
    if isinstance(cmd, str):
        cmd = cmd.split()
    return subprocess.Popen(cmd, *args, **kwargs)

def sh(cmd, *args, **kwargs):
    return sh_no_block(cmd, *args, stdout=subprocess.PIPE, **kwargs).communicate()[0]

# Wait until the processes have been shut down
while sh(f'pgrep -u {os.getuid()} -x polybar'):
    # Terminate already running bar instances
    sh('killall -q polybar')
    sleep(0.2)

# Launch bars
print(sh('printenv', env={}).decode('ascii'))
pids_dict = {'bottom': [], 'top': []}
# try:
xrandr = [line.decode('ascii').split() for line in sh('xrandr').splitlines()]
for line in xrandr:
    if 'connected' in line:
        print('Launching bar on ' + line[0] + (' (primary)' if 'primary' in line else ''))
        env = os.environ.copy()
        env['MONITOR'] = line[0]
        env['TRAY_POS'] = 'right' if 'primary' in line else ''
        # sh_no_block('polybar bottom')
        pids_dict['bottom'].append(sh_no_block('polybar bottom', env=env).pid)
        pids_dict['top'].append(sh_no_block('polybar top', env=env).pid)
for name, pids in pids_dict.items():
    with open(PID_FILE_FMT.format(name), 'w') as f:
        for pid in pids:
            f.write(str(pid) + '\n')
# except Exception as e:
#     print(e)
#     print('Launching bar')
#     env = os.environ.copy()
#     env['TRAY_POS'] = 'right'
#     sh_no_block('polybar bottom', env=env)
#     sh_no_block('polybar top', env=env)

print('Done')
