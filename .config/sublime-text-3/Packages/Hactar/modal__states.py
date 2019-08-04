import sublime
import sublime_plugin
import imp

# from . import modal__config as config
from . import modal__visual as visual
# config = imp.reload(config)
# visual = imp.reload(visual)
from .modal__config import (
    DEFAULT_STATE,
    INSERT_STATES,
    MOTION_STATES,
    SELECTION_STATE,
    STATE_SETTINGS,
)  # noqa: E402


def nonblank_selection(view):
    return any(not r.empty() for r in view.sel())


def on_state_change(view, force=False):
    settings = view.settings()
    # Don't do anything if it's a widget.
    if settings.get('is_widget'):
        settings.set('command_mode', False)
        return
    # Don't do anything if we haven't changed state (and the "force" flag isn't
    # specified).
    new_state = settings.get('edit_state', DEFAULT_STATE)
    old_state = settings.get('last_edit_state')
    if new_state == old_state and not force:
        return
    # Clear selection if necessary.
    if new_state == 'normal' and nonblank_selection(view):
        if old_state == SELECTION_STATE:
            pts = [sel.b for sel in view.sel()]
            view.sel().clear()
            for pt in pts:
                view.sel().add(sublime.Region(pt, pt))
        else:
            set_state(view, SELECTION_STATE)
    # Delete selected text if necessary.
    elif new_state == 'insert' and nonblank_selection(view):
        view.run_command('right_delete')
    # Update other settings.
    remove_state_watcher(view)
    settings.set('last_edit_state', new_state)
    settings.set('command_mode', new_state not in INSERT_STATES)
    visual.update_state(view)
    add_state_watcher(view)
    view.set_status('edit_state', new_state.upper())


def get_state(view):
    return view.settings().get('edit_state', DEFAULT_STATE)


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
        state = get_state(view)
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
            settings = view.settings()
            if settings.get('is_widget'):
                return False
            state = get_state(view)
            for mode in operand.split(','):
                mode = mode.strip()
                if mode == state:
                    return True
                if mode == 'motion' and state in MOTION_STATES:
                    return True
