from imp import reload
import sublime_plugin

from . import Hactar


class HactarReloadCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        reload(Hactar)
