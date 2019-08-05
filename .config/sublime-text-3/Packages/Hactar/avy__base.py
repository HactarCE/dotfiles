import sublime
import sublime_plugin


from .avy__config import LABEL_LETTERS
from .avy__utils import avy_seqs
from .avy__phantoms import make_phantoms


avy_states = {}


def get_avy_state(view):
    return avy_states.get(view.id())


def get_labels(n, *, allow_empty=True):
    return avy_seqs(n, LABEL_LETTERS, allow_empty=allow_empty)


class AvyState:
    """A class representing an Avy selection state."""

    def __init__(self, view, regions, callback, *, inline):
        if not regions:
            return
        self.view = view
        self.regions = regions
        self.labels = get_labels(len(regions), allow_empty=False)
        self.region_dict = dict(zip(self.labels, regions))
        self.callback = callback
        self.inline = inline
        self.phantom_set = sublime.PhantomSet(view)
        self.typed = ''
        view.settings().set('avy_active', 'hey')
        avy_states[view.id()] = self
        self.update()

    def backspace(self):
        if self.typed:
            self.typed = self.typed[:-1]
            self.update()
        else:
            self.cancel()

    def reset(self):
        self.typed = ''
        self.update()

    def feed_key(self, key):
        if any(s.startswith(self.typed + key) for s in self.labels):
            self.typed += key
            if self.typed in self.region_dict:
                self.confirm()
            else:
                self.update()
        else:
            self.cancel()

    def ensure_visible(self):
        self.view.set_viewport_position((0, self.view.viewport_position()[1]), False)

    def update(self):
        self.phantom_set.update(make_phantoms(
            self.view,
            self.region_dict,
            self.typed,
            inline=self.inline,
        ))
        sublime.set_timeout_async(self.ensure_visible, 0)

    def confirm(self):
        self.callback(self.region_dict[self.typed])
        self.cancel()

    def cancel(self):
        self.phantom_set.update([])
        self.view.settings().set('avy_active', False)
        del avy_states[self.view.id()]


class AvyFeedKey(sublime_plugin.TextCommand):
    """Feed a key to Avy."""

    def run(self, edit, key):
        avy = get_avy_state(self.view)
        if avy:
            avy.feed_key(key)


class AvyBackspace(sublime_plugin.TextCommand):

    def run(self, edit):
        avy = get_avy_state(self.view)
        if avy:
            avy.backspace()


class AvyCancel(sublime_plugin.TextCommand):

    def run(self, edit):
        avy = get_avy_state(self.view)
        if avy:
            avy.cancel()


class AvyStateListener(sublime_plugin.EventListener):
    def on_query_context(self, view, key, operator, operand, match_all):
        if key == 'avy_active':
            return view.id() in avy_states
