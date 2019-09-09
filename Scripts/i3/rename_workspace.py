#!/usr/bin/env python3

import utils

import renumber_workspaces

focused_workspace = utils.get_focused_workspace()

if 'all' in utils.args:
    prompt = f"Rename '{focused_workspace.name}'"
else:
    num, delim, old_name = utils.parse_workspace_name(focused_workspace.name)
    if num and 'hide-num' not in utils.args:
        prompt = f"Rename #{num} '{old_name}'"
    else:
        prompt = f"Rename '{old_name}'"

new_name = utils.dmenu([], prompt=prompt).strip()
print(new_name)
if new_name is not None:
    if 'all' not in utils.args:
        new_name = num + delim + new_name
    # TODO handle quotes in workspace names
    print(new_name, repr(new_name))
    utils.i3.command(f'rename workspace to "{new_name}"')
