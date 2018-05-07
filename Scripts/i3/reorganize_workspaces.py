#!/usr/bin/env python3

from shlex import quote as shellquote
import utils
from pprint import pprint as pp

outputs = utils.get_active_outputs()
for i in range(len(outputs)):
    workspaces = utils.get_workspaces_on_output(outputs[i].name)
    for j in range(len(workspaces)):
        print(i * 100 + j, workspaces[j].num)
        expected = i * 100 + j
        if workspaces[j].num != expected:
            print(f'renaming {workspaces[j].name}')
            _, _, name = utils.parse_workspace_name(workspaces[j].name)
            new_name = '{}:{}'.format(str(expected), name)
            print(new_name)
            utils.i3.command(f'rename workspace "{workspaces[j].name}" to "{new_name}"')
