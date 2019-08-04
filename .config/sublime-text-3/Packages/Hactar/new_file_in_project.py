# based on https://forum.sublimetext.com/t/default-folder-to-save-new-files/14812/4

import sublime_plugin


class NewFileListener(sublime_plugin.EventListener):
    def on_new_async(self, view):
        window = view.window()
        if window and window.folders():
            settings = view.settings()
            if not settings.get('default_dir'):
                settings.set('default_dir', window.folders()[0])


class PromptSaveInProject(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.settings().set('default_dir', self.view.window().folders()[0])
        self.view.run_command('prompt_save_as')
        print('oh')
