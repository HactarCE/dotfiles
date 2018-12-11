from subprocess import check_output, CalledProcessError
from shlex import split as shellsplit, quote as shellquote
import i3ipc
import os
import re
import sys

args = sys.argv[1:]

script_dir = os.path.dirname(os.path.realpath(__file__))

i3 = i3ipc.Connection()

def dmenu(items, prompt=None, **kwargs):
    command = ['rofi', '-dmenu']
    if prompt is not None:
        command += ['-p', prompt]
    for k, v in kwargs.items():
        print(k, v)
        command += ['-' + k, v]
    if isinstance(items, list):
        items = '\n'.join(items)
    if isinstance(items, str):
        items = items.encode('UTF-8')
    try:
        return check_output(command, input=items).decode('UTF-8')
    except CalledProcessError:
        return None

def i3_exec(command):
    i3.command('exec ' + command)

def i3_exec_nsi(command):
    i3_exec('--no-startup-id ' + command)

def get_focused_window():
    return i3.get_tree().find_focused()

def get_focused_workspace():
    return get_focused_window().workspace()

def get_focused_output():
    return next(ws for ws in i3.get_workspaces() if ws.focused).output

def get_active_outputs():
    return [output for output in i3.get_outputs() if output.active]

def get_workspaces_on_output(output):
    return [workspace for workspace in i3.get_workspaces() if workspace.output == output]

def parse_workspace_name(workspace_name):
    return re.match(r'^(\d*)(:?)(.+)$', workspace_name).groups()

def get_win_prop(prop_name, id=None):
    if not id:
        id = int(check_output(['xdotool', 'getactivewindow']))
    stdout = check_output(['xprop', prop_name.upper(), '-id', str(id)]).decode('UTF-8')
    output = stdout.partition(' = ')[-1].partition(',')[0].strip()
    if not output:
        raise Exception('Unable to acquire window property ' + prop_name,
                        'Could not handle this output:\n' + output)
    if output[0] == output[-1] == '"':
        output = output[1:-1]
    if output.isdigit():
        output = int(output)
    return output
