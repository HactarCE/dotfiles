import sublime
import sublime_plugin

import os
import shutil


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
		# 'caret_color': '#FF9933',
		'caret_color': '#FFCC00',
		'caret_style': 'solid',
		# 'caret_extra_bottom': 0,
		# 'caret_extra_top': 0,
		# 'caret_extra_width': 2,
		# 'wide_caret': False,
	},
	'insert': {
		'caret_color': '#33FF33',
		# 'caret_style': 'smooth',
		'caret_style': 'phase',
		# 'caret_extra_bottom': 2,
		# 'caret_extra_top': 2,
		# 'caret_extra_width': 1,
		# 'wide_caret': False,
	},
	'select': {
		'caret_color': '#00FFFF',
		'caret_style': 'solid',
	}
}

INSERT_STATES = ('insert', 'replace')
MOTION_STATES = ('normal', 'select')
SELECTION_STATE = 'select'


directory = os.path.join(os.path.dirname(__file__), COLOR_SCHEME_OVERRIDE_DIRECTORY)


if not os.path.isdir(directory):
	os.makedirs(directory)


def nonblank_selection(view):
	return any(not r.empty() for r in view.sel())

def on_state_change(view, force=False):
	print('whoa there')
	settings = view.settings()
	# Don't do anything if it's a widget
	if settings.get('is_widget'):
		settings.set('command_mode', False)
		return
	# Don't do anything if we haven't changed state (and the "force" flag isn't specified)
	new_state = settings.get('edit_state', DEFAULT_STATE)
	old_state = settings.get('last_edit_state')
	if new_state == 'normal' and nonblank_selection(view):
		if old_state == SELECTION_STATE:
			pts = [sel.b for sel in view.sel()]
			view.sel().clear()
			for pt in pts:
				view.sel().add(sublime.Region(pt, pt))
		else:
			set_state(view, SELECTION_STATE)
	elif new_state == 'insert' and settings.get('last_edit_state', None) == 'select' and nonblank_selection(view):
		view.run_command('right_delete')
	if (not force) and settings.get('last_edit_state', None) == settings.get('edit_state', DEFAULT_STATE):
		return
	remove_state_watcher(view)
	settings.set('last_edit_state', new_state)
	settings.set('command_mode', new_state not in INSERT_STATES)
	color_scheme_filename = os.path.splitext(os.path.split(settings.get('color_scheme'))[1])[0] + '.sublime-color-scheme'
	theme_file = os.path.join(directory, color_scheme_filename)
	for filename in os.listdir(directory):
		file = os.path.join(directory, filename)
		if not (os.path.isfile(theme_file) and os.path.samefile(file, theme_file)):
			os.remove(file)
	with open(theme_file, 'w') as f:
		if 'caret_color' in STATE_SETTINGS[new_state]:
			f.write(COLOR_SCHEME_OVERRIDE_TEMPLATE.format(STATE_SETTINGS[new_state]['caret_color']))
		else:
			f.write('{}')
	for k, v in STATE_SETTINGS[new_state].items():
		settings.set(k, v)
	add_state_watcher(view)
	view.set_status('edit_state', new_state.upper())

def set_state(view, new_state):
	settings = view.settings()
	if new_state not in STATE_SETTINGS:
		new_state = DEFAULT_STATE
	settings.set('edit_state', new_state)

def reset_state(view):
	set_state(view, DEFAULT_STATE)

def add_state_watcher(view):
	view.settings().add_on_change('edit_state_watcher', lambda: on_state_change(view))

def remove_state_watcher(view):
	view.settings().clear_on_change('edit_state_watcher')


class EditStateListener(sublime_plugin.EventListener):
	# def on_new(self, view):
	# 	print('new!')
	# 	set_state(settings, DEFAULT_STATE)
	# def on_clone(self, view):
	# 	set_state(view.settings(), DEFAULT_STATE)
	def on_activated(self, view):
		on_state_change(view, force=True)
	def on_deactivated(self, view):
		remove_state_watcher(view)
	def on_selection_modified(self, view):
		if (view.settings().get('edit_state') not in (SELECTION_STATE,) + INSERT_STATES
				and nonblank_selection(view)):
			set_state(view, 'select')
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
	def is_visible(self, args):
		return False
