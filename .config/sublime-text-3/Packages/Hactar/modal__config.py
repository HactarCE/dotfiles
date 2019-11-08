VISUAL_DIRNAME = '.CaretColor'

DEFAULT_STATE = 'insert'

INSERT_STATES = ('insert', 'replace')
MOTION_STATES = ('normal', 'select')
SELECTION_STATE = 'select'

VISUAL_TEMPLATE = '''\
{{
    "globals": {{
        "caret": "{}"
    }}
}}
'''

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
    },
    'horoline': {
        'caret_color': '#FF00FF',
        'caret_style': 'solid',
    }
}
