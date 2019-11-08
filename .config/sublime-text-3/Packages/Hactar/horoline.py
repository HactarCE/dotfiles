import sublime
import sublime_plugin

from .modal__states import get_state, set_state


# HoRoLine = Home Row Line jump (navigate to line using home row keys)


horoline_states = {}


def get_horoline_state(view):
    ret = horoline_states.get(view.id())
    if not ret:
        set_state('normal')
    return ret


class HorolineState:

    def __init__(self, view):
        self.view = view
        self.old_sel = list(self.view.sel())
        self.old_viewport = self.view.viewport_position()
        self.old_state = get_state(self.view)
        set_state(self.view, 'horoline')
        self.line_num = 0
        horoline_states[self.view.id()] = self

    def feed_digit(self, digit):
        self.line_num *= 10
        self.line_num += digit
        self.update()

    def backspace(self):
        if self.line_num:
            self.line_num //= 10
            self.update()
        else:
            self.cancel()

    def update(self):
        self.view.sel().clear()
        self.view.set_viewport_position(self.old_viewport)
        if self.line_num:
            text_point = sublime.Region(self.view.text_point(self.line_num - 1, 0))
            # self.view.sel().add(self.view.line(text_point))
            self.view.sel().add(text_point)
            # if not self.view.visible_region().contains(text_point):
            self.view.show_at_center(text_point)
        else:
            self.view.sel().add_all(self.old_sel)

    def cancel(self):
        self.line_num = 0
        self.confirm()

    def confirm(self):
        if self.line_num:
            self.old_state = 'normal'
        self.update()
        set_state(self.view, self.old_state)
        del horoline_states[self.view.id()]


class HorolineFeedKey(sublime_plugin.TextCommand):
    """Feed a key to Horoline."""

    def run(self, edit, digit):
        get_horoline_state(self.view).feed_digit(digit)


class HorolineBackspace(sublime_plugin.TextCommand):
    """Cancel a Horoline jump."""

    def run(self, edit):
        get_horoline_state(self.view).backspace()


class HorolineStartCommand(sublime_plugin.TextCommand):
    """Start a Horoline jump."""

    def run(self, edit):
        HorolineState(self.view)


class HorolineCancelCommand(sublime_plugin.TextCommand):
    """Cancel a Horoline jump."""

    def run(self, edit):
        get_horoline_state(self.view).cancel()


class HorolineConfirmCommand(sublime_plugin.TextCommand):
    """Confirm a Horoline jump."""

    def run(self, edit):
        get_horoline_state(self.view).confirm()
