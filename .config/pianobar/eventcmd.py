#!/usr/bin/env python3

EVENTCMD_FIFO_FILE = '~/.config/pianobar/eventcmd_fifo'

from utils import timeout
import os
import sys

EVENTCMD_FIFO_FILE = os.path.expanduser(EVENTCMD_FIFO_FILE)

try:
    with timeout(seconds=1):
        with open(EVENTCMD_FIFO_FILE, 'w') as f:
            f.write(sys.argv[1])
            f.write('\n')
            f.write(sys.stdin.read())
            f.write('\n~~~\n')
except TimeoutError:
    pass
