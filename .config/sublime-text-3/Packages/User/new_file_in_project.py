# from https://forum.sublimetext.com/t/default-folder-to-save-new-files/14812/4

import sublime_plugin

class NewFileListener(sublime_plugin.EventListener):
    def on_new_async(self, view):
        if view.window() and view.window().folders():
            view.settings().set('default_dir', view.window().folders()[0])
