import math
import sublime
import sublime_plugin


# LABEL_LETTERS = 'arstdhneio'
LABEL_LETTERS = 'abc'
LABEL_BASE = len(LABEL_LETTERS)


PHANTOM_STYLE = '''\
    <style type="text/css">
        .outer { padding-left: 2px; background-color: #66f; }
        .inner { padding: 0px, 4px; background-color: #339; }
        .discarded { background-color: #333 }
        .avy { padding: 0px; display: inline }
        .yes { color: #999; }
        .maybe { color: #fff; }
        .no { color: #f00; }
    </style>
'''


def common_prefix(a, b):
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            return a[:i]
    return a[:len(b)]


def make_phantom(location, yes, maybe, no, *, inline):
    # yes = letters typed already
    # maybe = letters that could be typed next
    # no = letters that can't be typed without backspacing
    container_html = '<div class="inner{}">{}</div>'
    container_html = '<div class="outer">{}</div>'.format(container_html)
    if no:
        inner_class = ' discarded'
    else:
        inner_class = ''
    paragraphs = ''
    if yes:
        paragraphs += '<pre class="avy yes">{}</pre>'.format(yes)
    if maybe:
        paragraphs += '<pre class="avy maybe"><u>{}</u>{}</pre>'.format(maybe[0], maybe[1:])
    if no:
        paragraphs += '<pre class="avy no">{}</pre>'.format(no)
    html = container_html.format(inner_class, paragraphs)
    html = '<html><body>{}</body>{}</html>'.format(html, PHANTOM_STYLE)
    layout = sublime.LAYOUT_INLINE if inline else sublime.LAYOUT_BELOW
    return sublime.Phantom(location, html, layout)


def make_phantoms(jump_spots, typed, *, inline):
    phantoms = []
    pad_length = max(map(len, jump_spots))
    for letters, location in jump_spots.items():
        letters += '&nbsp;' * (pad_length - len(letters))
        yes = common_prefix(letters, typed)
        maybe = letters[len(yes):]
        if yes == typed:
            no = ''
        else:
            maybe, no = '', maybe
        phantoms.append(make_phantom(location, yes, maybe, no, inline=inline))
    return phantoms


avy_states = {}


def get_avy_state(view):
    return avy_states.get(view.id())


def get_labels(n, *, allow_empty=True):
    if n == 1 and allow_empty:
        return ['']
    if n <= LABEL_BASE:
        return LABEL_LETTERS[:n]
    min_depth = int(math.log(n, LABEL_BASE))
    min_depth_leaves = LABEL_BASE ** min_depth
    node_amounts = [min_depth_leaves // LABEL_BASE] * LABEL_BASE
    extras = n - min_depth_leaves
    i = 0
    while extras:
        i -= 1
        amt = min(extras, LABEL_BASE ** min_depth - node_amounts[i])
        extras -= amt
        node_amounts[i] += amt
    assert(sum(node_amounts) == n)
    label_tails = map(get_labels, node_amounts)
    result = []
    for char, label_tails in zip(LABEL_LETTERS, label_tails):
        for tail in label_tails:
            result.append(char + tail)
    assert(len(result) == n)
    assert(len(result) == len(set(result)))
    return result


class AvyState:
    """A class representing an Avy selection state."""

    def __init__(self, view, regions, callback, *, inline):
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

    def update(self):
        self.phantom_set.update(make_phantoms(
            self.region_dict,
            self.typed,
            inline=self.inline,
        ))

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


class AvyJumpLineCommand(sublime_plugin.TextCommand):
    """Jump to a nearby line."""

    def run(self, edit, direction='both'):
        destinations = self.view.lines(self.view.visible_region())
        AvyState(self.view, destinations, self.callback, inline=True)

    def callback(self, region):
        self.view.sel().clear()
        self.view.sel().add(region)


class AvyStateListener(sublime_plugin.EventListener):
    def on_query_context(self, view, key, operator, operand, match_all):
        if key == 'avy_active':
            return view.id() in avy_states
