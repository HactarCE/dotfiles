#!/usr/bin/env python3

SETTINGS = [0.5, 1, 2, 3, 5, 10, 15, 20, 30, 50, 75, 100]

from subprocess import call, check_output
from sys import argv
from time import sleep

#output = check_output(['xbacklight', '-get'])
output = check_output(['light', '-G'])

try:
    backlight = float(output)
except:
    check_output(['notify-send', output])
    print(output)
    backlight = 50

i = min(range(len(SETTINGS)), key=lambda x: abs(SETTINGS[x] - backlight))
print(i, SETTINGS[i])

for arg in argv[1:]:
    if arg == '+':
        i += 1
    elif arg == '-':
        i -= 1

clamp = lambda *args: sorted(args)[1]
backlight = SETTINGS[clamp(0, i, len(SETTINGS) - 1)]

#call(['xbacklight', '-set', str(backlight)])
for i in range(2): # because polybar updates too quickly
    call(['light', '-S', str(backlight)])
    sleep(0.1)
