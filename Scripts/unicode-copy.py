#!/bin/env python3

from sys import argv
from clipboard import copy

copy(''.join(chr(int(arg, 16)) for arg in argv[1:]))
