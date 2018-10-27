#!/usr/bin/python
# -*- coding: utf-8 -*-

import sublime_plugin
import subprocess
from time import sleep
import sys

cl = lambda line: subprocess.Popen(line, shell=True, stdout=subprocess.PIPE).communicate()[0].strip()
log = lambda message: sys.stderr.write("Log: %s\n" % message)

sublimeMainWindowTitle = " - Sublime Text (UNREGISTERED)"

class LicenseWindowKiller(sublime_plugin.EventListener):

    active = True

    def seek_n_close(self):
        sublimePid = int(cl("""wmctrl -lp | grep "%s" | awk '{print $3}'""" % sublimeMainWindowTitle).decode())
        if sublimePid:
            sublimeMainWindowId = cl("""wmctrl -lp | grep "%s" | awk '{print $1}'""" % sublimeMainWindowTitle).decode()
            sublimeSecondWindowId = cl("""wmctrl -lp | grep %s | awk '{ids[$1]++}{for (id in ids){if (id != "%s"){printf id}}}'""" % (sublimePid, sublimeMainWindowId)).decode()
            if sublimeSecondWindowId:
                sublimeSecondWindowTitle = cl("""wmctrl -lp | grep %s | awk '{print $5}'""" % sublimeSecondWindowId).decode()
                if not sublimeSecondWindowTitle:
                    cl("wmctrl -i -c %s" % sublimeSecondWindowId)
                    return True
        return False

    def on_pre_save_async(self, *args):
        counter = 25
        while self.active:
            sleep(.2)
            counter -= 1
            if counter < 0:
                self.active = False
            self.active = not self.seek_n_close()