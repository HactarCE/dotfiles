from subprocess import CalledProcessError, check_output
from time import sleep
import os
import sublime_plugin


ST3_PID = os.getppid()


def run(command):
    return check_output(command.split()).decode().strip()


class LicensePopupKiller(sublime_plugin.EventListener):
    """Kill the ST3 license popup on save."""

    def try_kill_popup(self):
        try:
            win_ids = map(int, run('xdotool search --pid {}'.format(ST3_PID)).splitlines())
        except CalledProcessError:
            return False
        for win_id in win_ids:
            title = run('xdotool getwindowname {}'.format(win_id))
            if not title:
                run('xdotool windowclose {}'.format(win_id))

    def on_pre_save_async(self, *args):
        for i in range(5):
            sleep(.2)
            if self.try_kill_popup():
                break
