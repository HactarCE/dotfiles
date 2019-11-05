#!/usr/bin/env python3

import signal
import sys
import re


def display_status(status=None, size=''):
    with open('/tmp/pcloud_polybar_status', 'w') as f:
        f.write({
            None: '',
            'READY': '',
            'SCANNING': '痢',
            'UPLOADING': f'',
            'DOWNLOADING': f'',
            'DOWNLOADINGANDUPLOADING': f'痢',
        }.get(status, f'unknown status: {status}'))
        if size:
            f.write(f' {size}')


# Set status when killed

def sigterm_handler(signal, frame):
    display_status(None)
    sys.exit(0)


signal.signal(signal.SIGTERM, sigterm_handler)


display_status(None)

for line in sys.stdin:
    re_status_result = re.search(r'status is ([A-Z]+)', line)
    if not re_status_result:
        print('')
        continue
    status = re_status_result.group(1)
    re_size_results = re.findall(r'Remaining: \d+ files, ([a-z0-9A-Z.]+) ', line)
    size = sum(int(m.group(1)) for m in re_size_results)
    display_status(status, size)

display_status(None)
