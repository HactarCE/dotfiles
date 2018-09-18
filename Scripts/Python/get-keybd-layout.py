#!/bin/env python3

from subprocess import check_output
import re

s1 = check_output(['setxkbmap', '-query']).decode()
if 'variant:' in s1:
	s2 = re.search(r'variant:\s+([^\n]+)', s1).group(1)
	print(s2.title())
else:
	print('Qwerty ')
