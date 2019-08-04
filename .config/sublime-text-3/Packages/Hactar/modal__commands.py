import imp
import sublime
import sublime_plugin

# from . import modal__states
# imp.reload(modal__states)
from .modal__states import (
    get_state,
    set_state,
    INSERT_STATES,
    MOTION_STATES,
    SELECTION_STATE,
)  # noqa: E402


class ExtendableMotionCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        args['extend'] = self.view.settings().get('edit_state') == SELECTION_STATE
        self.view.run_command(args.pop('command'), args)


class LinewiseCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        self.view.run_command('expand_selection', {'to': 'line'})
        self.view.run_command(args.pop('command'), args)


class ModalInsertLineCommand(sublime_plugin.TextCommand):
    def run(self, edit, place='here', insert=False):
        sel = self.view.sel()
        self.view.add_regions('_hactar_modal_tmp', sel, flags=sublime.HIDDEN)
        if place == 'above':
            for r in sel:
                sel.subtract(r)
                sel.add(sublime.Region(r.begin()))
            self.view.run_command('move_to', {'to': 'hardbol'})
            self.view.run_command('insert', {'characters': '\n'})
            self.view.run_command('move', {'by': 'lines', 'forward': False})
        elif place == 'below':
            for r in sel:
                sel.subtract(r)
                if r.size() > 1 and self.view.rowcol(r.end())[1] == 0:
                    sel.add(sublime.Region(r.end() - 1))
                else:
                    sel.add(sublime.Region(r.end()))
            self.view.run_command('move_to', {'to': 'hardeol'})
            self.view.run_command('insert', {'characters': '\n'})
        else:
            for r in sel:
                if r.size() > 1 and self.view.rowcol(r.end())[1] == 0:
                    sel.subtract(r)
                    sel.add(sublime.Region(r.begin(), r.end() - 1))
            self.view.run_command('expand_selection', {'to': 'line'})
            self.view.run_command('delete_left')
            self.view.run_command('insert', {'characters': '\n'})
            self.view.run_command('move', {'by': 'lines', 'forward': False})
        if insert:
            self.view.run_command('reindent', {'single_line': True, 'force_indent': False})
            set_state(self.view, 'insert')
        else:
            self.view.run_command('delete_to', {'to': 'hardbol'})
            sel.clear()
            for r in self.view.get_regions('_hactar_modal_tmp'):
                sel.add(r)
