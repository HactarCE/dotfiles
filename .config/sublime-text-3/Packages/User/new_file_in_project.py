# from https://forum.sublimetext.com/t/default-folder-to-save-new-files/14812/4

import sublime_plugin

class NewFileListener(sublime_plugin.EventListener):
    def on_new_async(self, view):
        window = view.window()
        if window and window.folders():
            settings = view.settings()
            if not settings.get('default_dir'):
                settings.set('default_dir', window.folders()[0])
