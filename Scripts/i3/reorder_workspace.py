#!/usr/bin/env python3

import utils

import reorganize_workspaces

workspaces = utils.get_workspaces_on_output(utils.get_focused_output())
from pprint import pprint as pp
focused = utils.get_focused_workspace().num % 100

def swap_workspaces(ws1, ws2):
    print(ws1, ws2)
    ws1, ws2 = workspaces[ws1].name, workspaces[ws2].name
    ws1_parsed = utils.parse_workspace_name(ws1)
    ws2_parsed = utils.parse_workspace_name(ws2)
    new_ws1 = ws2_parsed[0] + ''.join(ws1_parsed[1:])
    new_ws2 = ws1_parsed[0] + ''.join(ws2_parsed[1:])
    # print(f'{ws1}, {ws2} becomes {new_ws2}, {new_ws1}')
    utils.i3.command(f'rename workspace "{ws1}" to _temp')
    utils.i3.command(f'rename workspace "{ws2}" to "{new_ws2}"')
    utils.i3.command(f'rename workspace _temp to "{new_ws1}"')

for arg in utils.args:
    print(focused, len(workspaces))
    if arg == 'left' and focused > 0:
        swap_workspaces(focused, focused - 1)
    elif arg == 'right' and focused < len(workspaces) - 1:
        swap_workspaces(focused, focused + 1)
