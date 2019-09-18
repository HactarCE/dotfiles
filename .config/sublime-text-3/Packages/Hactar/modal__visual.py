from os import path
import os

from .modal__config import (
    VISUAL_DIRNAME,
    VISUAL_TEMPLATE,
    STATE_SETTINGS,
    DEFAULT_STATE,
)


VISUAL_DIR = path.join(path.dirname(__file__), VISUAL_DIRNAME)

try:
    os.makedirs(r'/tmp/ST3-edit-states')
except OSError:
    pass

try:
    os.symlink(r'/tmp/ST3-edit-states', VISUAL_DIR)
except OSError:
    pass


def update_state(view):
    settings = view.settings()
    edit_state = settings.get('edit_state', DEFAULT_STATE)
    color_scheme_filename = path.splitext(path.split(settings.get('color_scheme'))[1])[0] + '.sublime-color-scheme'
    theme_file = path.join(VISUAL_DIR, color_scheme_filename)
    with open(theme_file, 'w') as f:
        if 'caret_color' in STATE_SETTINGS[edit_state]:
            f.write(VISUAL_TEMPLATE.format(STATE_SETTINGS[edit_state]['caret_color']))
        else:
            f.write('{}')
    for k, v in STATE_SETTINGS[edit_state].items():
        settings.set(k, v)
