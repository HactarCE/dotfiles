#!/bin/env python3

SETTINGS = [0.5, 1, 2.5, 5, 10, 15, 20, 30, 50, 75, 100]

from subprocess import call, check_output
from utils import args

output = check_output(['xbacklight', '-get'])

try:
    backlight = float(output)
except:
    backlight = 50

i = min(range(len(SETTINGS)), key=lambda x: abs(SETTINGS[x] - backlight))
print(i, SETTINGS[i])

for arg in args:
    if arg == '+':
        i += 1
    elif arg == '-':
        i -= 1

clamp = lambda *args: sorted(args)[1]
backlight = SETTINGS[clamp(0, i, len(SETTINGS) - 1)]

call(['xbacklight', '-set', str(backlight)])
