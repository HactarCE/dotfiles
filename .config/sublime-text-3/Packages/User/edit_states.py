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


if os.path.isdir(directory):
	for filename in os.listdir(directory):
		file = os.path.join(directory, filename)
		os.remove(file)
else:
	os.makedirs(directory)


def nonblank_selection(view):
	return any(not r.empty() for r in view.sel())

def on_state_change(view, force=False):
	settings = view.settings()
	# Don't do anything if it's a widget
	if settings.get('is_widget'):
		settings.set('command_mode', False)
		return
	# Don't do anything if we haven't changed state (and the "force" flag isn't specified)
	new_state = settings.get('edit_state', DEFAULT_STATE)
	old_state = settings.get('last_edit_state')
	if (not force) and settings.get('last_edit_state', None) == settings.get('edit_state', DEFAULT_STATE):
		return
	if new_state == 'normal' and nonblank_selection(view):
		if old_state == SELECTION_STATE:
			pts = [sel.b for sel in view.sel()]
			view.sel().clear()
			for pt in pts:
				view.sel().add(sublime.Region(pt, pt))
		else:
			set_state(view, SELECTION_STATE)
	elif new_state == 'insert' and nonblank_selection(view):
		view.run_command('right_delete')
	remove_state_watcher(view)
	settings.set('last_edit_state', new_state)
	settings.set('command_mode', new_state not in INSERT_STATES)
	color_scheme_filename = os.path.splitext(os.path.split(settings.get('color_scheme'))[1])[0] + '.sublime-color-scheme'
	theme_file = os.path.join(directory, color_scheme_filename)
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
		state = view.settings().get('edit_state')
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
		# remove_state_watcher(self.view)
		# print('rem')
		self.view.run_command(args.pop('command'), args)
		# if args['extend'] and not nonblank_selection(self.view):
		# 	print('change')
		# 	remove_state_watcher(self.view)
		# 	def handler():
		# 		print('fake handle! ha!')
		# 		remove_state_watcher(self.view, 'zz_edit_state_watcher')
		# 		add_state_watcher(self.view)
		# 	add_state_watcher(self.view, 'zz_edit_state_watcher', handler)
		# set_state(self.view, SELECTION_STATE)
		# print('add')
		# add_state_watcher(self.view)
	def is_visible(self, args):
		return False


class LinewiseCommand(sublime_plugin.TextCommand):
	def run(self, edit, **args):
		self.view.run_command('expand_selection', {'to': 'line'})
		self.view.run_command(args.pop('command'), args)
	def is_visible(self, args):
		return False


class ModalInsertLineCommand(sublime_plugin.TextCommand):
	def run(self, edit, place='here', insert='false'):
		old_regions = [r for r in self.view.sel()]
		# for r in self.view.sel():
		# 	self.view.
		self.view.add_regions('_caret_temp', self.view.sel(), flags=sublime.HIDDEN)
		below = place == 'below'
		above = place == 'above'
		here = place not in ('below', 'above')
		insert = insert == 'true'
		if here:
			self.view.run_command('expand_selection', {'to': 'line'})
			above = True
		if above:
			self.view.run_command('move_to', {'to': 'hardbol'})
		if below:
			self.view.run_command('move_to', {'to': 'hardeol'})
		self.view.run_command('insert', {'characters': '\n'})
		if place == 'above':
			self.view.run_command('move', {'by': 'lines', 'forward': False})
		self.view.run_command('reindent')
		# else:
		# 	# self.
		# 	self.view.run_command('')
		if insert:
			# if not forward:
			set_state(self.view, 'insert')
		else:
			self.view.sel().clear()
			for r in self.view.get_regions('_caret_temp'):
				self.view.sel().add(r)
				print('adding old')
		self.view.erase_regions('_caret_temp')
	def is_visible(self, args):
		return False
