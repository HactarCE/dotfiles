#!/usr/bin/env python3

import utils
import re
import sys

workspaces = utils.i3.get_workspaces()

if '-' in utils.args:
    destination = utils.args[utils.args.index('-') + 1]
elif 'new' not in utils.args:
    destination = 'New'
    prompt = ('Move' if 'move' in utils.args else 'Switch') + ' to'
    workspace_names = sorted(set(utils.parse_workspace_name(ws.name)[-1] for ws in utils.i3.get_workspaces()))
    active_workspace = utils.get_focused_workspace().name
    active_row = workspace_names.index(utils.parse_workspace_name(active_workspace)[-1])
    destination_name = utils.dmenu(workspace_names, prompt=prompt, a=str(active_row)).strip()
    try:
        destination = next(ws.name for ws in workspaces if utils.parse_workspace_name(ws.name)[-1] == destination_name)
    except:
        destination = destination_name

print(destination)

if destination:
    utils.i3.command(f'{"move container to" if "move" in utils.args else ""} workspace "{destination}"')
    import reorganize_workspaces
