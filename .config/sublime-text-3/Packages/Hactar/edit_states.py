from os import path
import os
import sublime
import sublime_plugin


COLOR_SCHEME_OVERRIDE_DIRECTORY = '.CursorColor'

COLOR_SCHEME_OVERRIDE_TEMPLATE = '''\
{{
    "globals": {{
        "caret": "{}"
    }}
}}
'''

DEFAULT_STATE = 'normal'

STATE_SETTINGS = {
    'normal': {
        'caret_color': '#FFCC00',
        'caret_style': 'solid',
    },
    'insert': {
        'caret_color': '#33FF33',
        'caret_style': 'phase',
    },
    'select': {
        'caret_color': '#00FFFF',
        'caret_style': 'solid',
    }
}

INSERT_STATES = ('insert', 'replace')
MOTION_STATES = ('normal', 'select')
SELECTION_STATE = 'select'


directory = path.join(path.dirname(__file__), COLOR_SCHEME_OVERRIDE_DIRECTORY)


try:
    os.makedirs(r'/dev/shm/ST3-edit-states')
except OSError:
    pass
try:
    os.symlink(r'/dev/shm/ST3-edit-states', directory)
except OSError:
    pass
try:
    for file in os.listdir(directory):
        os.remove(path.join(directory, file))
except OSError:
    pass


def nonblank_selection(view):
    return any(not r.empty() for r in view.sel())


def on_state_change(view, force=False):
    settings = view.settings()
    # Don't do anything if it's a widget
    if settings.get('is_widget'):
        settings.set('command_mode', False)
        return
    # Don't do anything if we haven't changed state (and the "force" flag isn't specified)
    new_state = settings.get('edit_state', DEFAULT_STATE)
    old_state = settings.get('last_edit_state')
    if (not force) and settings.get('last_edit_state', None) == settings.get('edit_state', DEFAULT_STATE):
        return
    if new_state == 'normal' and nonblank_selection(view):
        if old_state == SELECTION_STATE:
            pts = [sel.b for sel in view.sel()]
            view.sel().clear()
            for pt in pts:
                view.sel().add(sublime.Region(pt, pt))
        else:
            set_state(view, SELECTION_STATE)
    elif new_state == 'insert' and nonblank_selection(view):
        view.run_command('right_delete')
    remove_state_watcher(view)
    settings.set('last_edit_state', new_state)
    settings.set('command_mode', new_state not in INSERT_STATES)
    color_scheme_filename = path.splitext(path.split(settings.get('color_scheme'))[1])[0] + '.sublime-color-scheme'
    theme_file = path.join(directory, color_scheme_filename)
    with open(theme_file, 'w') as f:
        if 'caret_color' in STATE_SETTINGS[new_state]:
            f.write(COLOR_SCHEME_OVERRIDE_TEMPLATE.format(STATE_SETTINGS[new_state]['caret_color']))
        else:
            f.write('{}')
    for k, v in STATE_SETTINGS[new_state].items():
        settings.set(k, v)
    # view.add_regions('edit_state_cursor', [r for r in view.sel()] + [sublime.Region(1, 1)], 'edit-state.' + new_state, '', sublime.DRAW_EMPTY)
    # print('edit-state.' + new_state)
    # view.get_regions('edit_state_cursor')
    add_state_watcher(view)
    view.set_status('edit_state', new_state.upper())


def set_state(view, new_state):
    settings = view.settings()
    if new_state not in STATE_SETTINGS:
        new_state = DEFAULT_STATE
    settings.set('edit_state', new_state)


def reset_state(view):
    set_state(view, DEFAULT_STATE)


def add_state_watcher(view, name='edit_state_watcher', handler=None):
    view.settings().add_on_change(name, handler or (lambda: on_state_change(view)))


def remove_state_watcher(view, name='edit_state_watcher'):
    view.settings().clear_on_change(name)


class EditStateListener(sublime_plugin.EventListener):
    def on_activated(self, view):
        on_state_change(view, force=True)

    def on_deactivated(self, view):
        remove_state_watcher(view)

    def on_selection_modified(self, view):
        state = view.settings().get('edit_state')
        if state not in INSERT_STATES:
            if nonblank_selection(view):
                if state != SELECTION_STATE:
                    # print('to sel')
                    set_state(view, SELECTION_STATE)
            else:
                if state == SELECTION_STATE:
                    # print('to norm')
                    set_state(view, 'normal')

    def on_query_context(self, view, key, operator, operand, match_all):
        if key == 'edit_state':
            get = view.settings().get
            if get('is_widget'): return False
            current_mode = get('edit_state', DEFAULT_STATE)
            for mode in operand.split(','):
                mode = mode.strip()
                if mode == current_mode:
                    return True
                if mode == 'motion' and current_mode in MOTION_STATES:
                    return True


class ExtendableMotionCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        args['extend'] = self.view.settings().get('edit_state') == SELECTION_STATE
        self.view.run_command(args.pop('command'), args)

    # def is_visible(self, args):
    #     return False


class LinewiseCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        self.view.run_command('expand_selection', {'to': 'line'})
        self.view.run_command(args.pop('command'), args)

    # def is_visible(self, args):
    #     return False


class ModalInsertLineCommand(sublime_plugin.TextCommand):
    def run(self, edit, place='here', insert=False):
        # TODO base current line on selection rather than cursor
        self.view.add_regions('_caret_temp', self.view.sel(), flags=sublime.HIDDEN)
        below = place == 'below'
        above = place == 'above'
        here = place not in ('below', 'above')
        print(place)
        if here:
            self.view.run_command('run_macro_file', {'file': 'res://Packages/Default/Delete Line.sublime-macro'})
            above = True
        if above:
            self.view.run_command('move_to', {'to': 'hardbol'})
        if below:
            self.view.run_command('move_to', {'to': 'hardeol'})
        self.view.run_command('insert', {'characters': '\n'})
        if above:
            self.view.run_command('move', {'by': 'lines', 'forward': False})
        self.view.run_command('reindent', {'single-line': True, 'force_indent': False})
        if insert:
            set_state(self.view, 'insert')
        else:
            self.view.sel().clear()
            for r in self.view.get_regions('_caret_temp'):
                self.view.sel().add(r)
            # TODO adding line below while at EoL causes cursor to move to new line
        self.view.erase_regions('_caret_temp')

    # def is_visible(self, args):
    #     return False
