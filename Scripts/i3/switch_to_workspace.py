#!/usr/bin/env python3

import utils
import re
import sys

workspaces = utils.i3.get_workspaces()

destination = 'New'
if '-' in utils.args:
    destination = utils.args[utils.args.index('-') + 1]
elif 'new' not in utils.args:
    prompt = '{} to:'.format('Move' if 'move' in utils.args else 'Switch')
    workspace_names = set(utils.parse_workspace_name(ws.name)[-1] for ws in utils.i3.get_workspaces())
    workspace_names = sorted(workspace_names)
    # workspace_names = [ws.name for ws in workspaces]
    destination_name = utils.dmenu(workspace_names, prompt=prompt).strip()
    try:
        destination = next(ws.name for ws in workspaces if utils.parse_workspace_name(ws.name)[-1] == destination_name)
    except:
        destination = destination_name

print(destination)

if destination:
    utils.i3.command(f'{"move container to" if "move" in utils.args else ""} workspace "{destination}"')
    import reorganize_workspaces
