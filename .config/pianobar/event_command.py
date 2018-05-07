#!/usr/bin/env python3

from subprocess import check_output
import sys

info = sys.stdin.readlines()
print()
print('----- from PYTHON')
print('args:', sys.argv[1:])
print(info)
print('----- done')
print()

# check_output(['notify-send', sys.argv[1], info])
