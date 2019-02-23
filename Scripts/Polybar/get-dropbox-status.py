#!/usr/bin/env python3

from subprocess import check_output

output = check_output(['dropbox-cli', 'status']).decode('UTF-8')

output_starts_with = lambda s: output.lower().startswith(s)

first_line = ' ' + output.splitlines()[0]

if output_starts_with('up to date'):
    print('')
elif output_starts_with(('indexing', 'syncing')):
    print('מּ' + first_line)
elif output_starts_with('downloading'):
    print('' + first_line)
elif output_starts_with('uploading'):
    print('' + first_line)
elif output_starts_with("can't"):
    print('')
else:
    print('')
