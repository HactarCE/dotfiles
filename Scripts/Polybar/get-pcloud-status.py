#!/usr/bin/env python3

from subprocess import check_output
import re

output = check_output(['tail', '-1', '/home/andrew/Testing/pcloud.log']).decode('UTF-8')

re_result = re.search(r'status is ([A-Z]+)', output)

amount = re.search(r'Remaining: \d+ files, ([a-z0-9A-Z.]+) ', output)

if re_result:
    status = re_result.group(1)
else:
    print('')

if amount:
    amount = amount.group(1)


print({
    'READY': '',
    'SCANNING': '痢',
    'UPLOADING': f' {amount}',
    'DOWNLOADING': f' {amount}',
    'DOWNLOADINGANDUPLOADING': '痢',
}.get(status, ''))

# if output_starts_with('up to date'):
#     print('')
# elif output_starts_with(('indexing', 'syncing')):
#     print('מּ' + first_line)
# elif output_starts_with('downloading'):
#     print('' + first_line)
# elif output_starts_with('uploading'):
#     print('' + first_line)
# elif output_starts_with("can't"):
#     print('')
# else:
#     print('')
