from collections import defaultdict
import sublime

from .avy__config import PHANTOM_STYLE
from .avy__utils import common_prefix


def make_phantom(location, yes, maybe, no, *, inline, include_body=False):
    # yes = letters typed already
    # maybe = letters that could be typed next
    # no = letters that can't be typed without backspacing
    container_html = '<div class="outer"><div class="inner{}">{}</div></div>'
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
    if include_body:
        html = '<html><body>{}</body>{}</html>'.format(html, PHANTOM_STYLE)
    layout = sublime.LAYOUT_INLINE if inline else sublime.LAYOUT_BELOW
    return sublime.Phantom(location, html, layout)


def merge_phantoms_by_line(view, phantoms):
    by_rowcol = defaultdict(lambda: {})
    for phantom in phantoms:
        row, col = view.rowcol(phantom.region.begin())
        by_rowcol[row][col] = phantom.content
    new_phantoms = []
    for row, by_col in by_rowcol.items():
        if len(by_col) <= 1:
            new_phantoms += by_col.values()
        else:
            html = ''
            for col, content in by_col.items():
                # html += '<div style="position: relative; left: {}em">{}</div>'.format(col, content)
                html += content
            html = '<html><body>{}</body>{}</html>'.format(html, PHANTOM_STYLE)
            print(html)
            new_phantoms.append(sublime.Phantom(sublime.Region(view.text_point(row, 0)), content, sublime.LAYOUT_BLOCK))
    return new_phantoms


def make_phantoms(view, jump_spots, typed, *, inline):
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
        phantoms.append(make_phantom(location, yes, maybe, no, inline=inline, include_body=inline))
    if inline:
        return phantoms
    else:
        # return merge_phantoms_by_line(view, phantoms)
        ph = merge_phantoms_by_line(view, phantoms)
        return ph
