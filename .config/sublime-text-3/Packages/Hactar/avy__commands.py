import sublime
import sublime_plugin

from .avy__base import AvyState


class AvyJumpLineCommand(sublime_plugin.TextCommand):
    """Jump to a nearby line."""

    def run(self, edit, direction='both'):
        destinations = self.view.lines(self.view.visible_region())
        sel = self.view.sel()[0]
        if direction == 'up':
            destinations = [d for d in destinations if d.end() < sel.begin()]
            destinations.reverse()
        if direction == 'down':
            destinations = [d for d in destinations if d.begin() > sel.end()]
        AvyState(self.view, destinations, self.callback, inline=True)

    def callback(self, region):
        self.view.sel().clear()
        self.view.sel().add(sublime.Region(region.a))
        # self.view.sel().add(region)


class AvyJumpSubwordCommand(sublime_plugin.TextCommand):
    """Jump to a subword within the line."""

    def run(self, edit):
        destinations = []
        total = self.view.line(self.view.sel()[0])
        i = total.begin()
        start_flags = sublime.CLASS_SUB_WORD_START + sublime.CLASS_WORD_START
        end_flags = sublime.CLASS_SUB_WORD_END + sublime.CLASS_WORD_END
        while i < total.end():
            begin = i = self.view.find_by_class(i - 1, True, start_flags)
            end = i = self.view.find_by_class(i, True, end_flags)
            if i <= total.end():
                destinations.append(sublime.Region(begin, end))
        AvyState(self.view, destinations, self.callback, inline=False)

    def callback(self, region):
        self.view.sel().clear()
        self.view.sel().add(region)
