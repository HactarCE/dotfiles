#!/usr/bin/env python3

from sys import argv
from utils import i3, i3_exec_nsi, get_focused_window

def format_con(con):
    return con.name or con.layout or con.type

def print_con(c):
    print(c.workspace().name, c.type, c.name, c.layout, c.nodes[0].layout)

def find_unsimplified():
    for wksp in i3.get_tree().workspaces():
        for node in wksp.nodes:
            n = find_unsimplified_within(node)
            if n:
                return n

def find_unsimplified_within(con):
    # print('leaves:', [c.name for c in con.leaves()])
    if len(con.nodes) == 1 and con.type != 'workspace':
        return con
    else:
        for child in con.nodes:
            print('testing', format_con(child))
            c = find_unsimplified_within(child)
            print('done with', format_con(child))
            if c:
                return c

original_focus = get_focused_window()

limit = 3
count = 0
workspaces = []
while count < limit and find_unsimplified():
    c = find_unsimplified()
    focused_window = get_focused_window()
    print_con(c)
    # print_con(c.nodes[0])
    print(f"Resolving redundancy on '{c.workspace().name}' ({format_con(c.nodes[0])} inside {format_con(c)}) ...")
    c.nodes[0].command('focus; move {}'.format('up' if c.orientation == 'vertical' else 'left'))
    # This shouldn't be necessary ...
    if c.parent.type == 'workspace':
        c.nodes[0].command('move left; move up')
    focused_window.command('focus')
    count += 1
    workspaces.append(c.workspace().name)

if count < limit:
    print("Maximum corrections reached; run script again to resolve more.")

print(f"{count} redundanc{'y has' if count == 1 else 'ies have'} been resolved.")
print(f"Returning focus to {format_con(original_focus)} ...")
original_focus.command('focus')

if 'notify' in argv[1:]:
    from utils import check_output
    message = f"{count or 'No'} container redundanc{'y' if count == 1 else 'ies'} {'resolved' if count else 'exist'}"
    sub_text = '\n'.join(workspaces)
    if count >= limit:
        sub_text += "\n\nRun the script again to resolve more"
    check_output(['notify-send', '-t', '2000', message, sub_text])
