#!/usr/bin/env python3

from subprocess import call, check_output, CalledProcessError, TimeoutExpired
from shlex import split as shellsplit, quote as shellquote
from time import time
import i3ipc
import os
import re
import sys

args = sys.argv[1:]

script_dir = os.path.dirname(os.path.realpath(__file__))

i3 = i3ipc.Connection()

def dmenu(items, prompt=None, **kwargs):
    command = ['rofi', '-dmenu', '-i']
    if not items:
        command += ['-l', '-1']
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

def get_win_prop(prop_name, win_id=None):
    if not win_id:
        win_id = get_active_window_id()
    stdout = check_output(['xprop', prop_name.upper(), '-id', str(win_id)]).decode('UTF-8')
    output = stdout.partition(' = ')[-1].partition(',')[-1].strip()
    if not output:
        raise Exception('Unable to acquire window property ' + prop_name,
                        'Could not handle this output:\n' + output)
    if output[0] == output[-1] == '"':
        output = output[1:-1]
    if output.isdigit():
        output = int(output)
    return output



def xdotool(action):
    return call(['xdotool'] + action)

def get_active_window_id():
    return check_output(['xdotool', 'getactivewindow']).strip()

def get_xwininfo(win_id):
    return check_output(['xwininfo', '-id', win_id]).decode('utf-8')

def get_map_state(win_id):
    """Returns either 'IsUnviewable', 'IsViewable', or 'IsUnMapped'"""
    return re.search(r'\n  Map State: (\w+)\n', get_xwininfo(win_id)).group(1)



def win_is_mapped(win_id):
    return get_map_state(win_id).lower() != 'isunmapped'

def win_is_visible(win_id):
    return get_map_state(win_id).lower() == 'isviewable'

def win_is_active(win_id):
    return get_active_window_id() == win_id



def win_close(win_id=None):
    return xdotool(['windowclose', win_id or get_active_window_id()])

def win_kill(win_id=None):
    return xdotool(['windowkill', win_id or get_active_window_id()])

def win_focus(win_id, sync=True):
    return xdotool(('windowfocus' + (' --sync' if sync else '')).split() + [win_id])

def win_map(win_id, sync=True):
    return xdotool(('windowmap' + (' --sync' if sync else '')).split() + [win_id])

def win_unmap(win_id, sync=True):
    return xdotool(('windowunmap' + (' --sync' if sync else '')).split() + [win_id])

def win_hacky_unfocus(win_id=None):
    if win_id == None:
        win_id = get_active_window_id()
    win_activate(win_id)
    win_unmap(win_id)
    new_focus = get_active_window_id()
    win_map(win_id)
    xdotool(['windowactivate', new_focus], True)



class MultiPressChecker:

    def __init__(self, filename, timeout=0.5):
        self.filename = filename
        self.timeout = timeout
        self.presses = None

    def __enter__(self):
        try:
            with open(self.filename, 'r+') as f:
                self.read_data(f)
                if abs(time() - self.time) > self.timeout * 2:
                    raise Exception("File is too old")
                self.presses += 1
                self.write_data(f)
            self.first = False
        except:
            self.first = True
            with open(self.filename, 'w') as f:
                self.presses = 1
                self.time = time()
                self.write_data(f)
        return self

    def read_data(self, fileobject):
        f = fileobject
        filetime, filepresses = f.read().split()
        self.time = float(filetime)
        self.presses = int(filepresses)

    def write_data(self, fileobject):
        f = fileobject
        f.seek(0)
        f.write(str(self.time) + ' ' + str(self.presses))
        f.truncate()

    def get_wait_time(self):
        with open(self.filename) as f:
            self.read_data(f)
        return self.time + self.timeout - time()

    def wait(self, press_count=None):
        print(self.presses)
        try:
            wait_time = self.get_wait_time()
            while wait_time > 0:
                if press_count and self.presses >= press_count:
                    return True
                call(['inotifywait', '-e', 'modify', self.filename], timeout=wait_time)
                wait_time = self.get_wait_time()
        except TimeoutExpired:
            return press_count and self.presses >= press_count

    def __exit__(self, type, value, traceback):
        if self.first:
            if self.timeout > 0:
                self.wait()
            os.remove(self.filename)
