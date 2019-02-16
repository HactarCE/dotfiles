#!/usr/bin/env python3

from subprocess import check_output

output = check_output(['dropbox-cli', 'status']).decode('UTF-8').lower()

def get_number():
    s = ''.join(c for c in output if c in '0123456789')
    if s:
        return ' ' + s
    else:
        return ''

first_line = ' ' + output.splitlines()[0]

if output.startswith('up to date'):
    print('')
elif output.startswith(('indexing', 'syncing')):
    print('מּ' + first_line)
elif output.startswith('downloading'):
    print('' + first_line)
elif output.startswith('uploading'):
    print('' + first_line)
elif output.startswith("can't"):
    print('')
else:
    print('')
