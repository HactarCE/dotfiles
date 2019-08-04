import sublime_plugin


print('hi!')
class HactarReload(sublime_plugin.ApplicationCommand):
    def run(self, *args):
        print(args)
        print('run forrest run')

    def description(self, *args):
        print(args)
        return "Reload Hactar plugins"

    def is_visible(self, *args):
        print(args)
        return True
