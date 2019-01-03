#!/usr/bin/env python3

from subprocess import call, check_output
from utils import rofi, subtext

def autorandr(*args, **kwargs):
    return check_output(['autorandr', '--skip-options', 'gamma'] + list(args), **kwargs).decode()

def show_autorandrofi(only_detected=True):

    autorandr_detected = [s.strip() for s in autorandr('--detected').splitlines()]
    if only_detected:
        configurations = autorandr_detected
    else:
        autorandr_all = [s.strip() for s in autorandr().splitlines()]
        configurations = [s.rpartition(' (detected)')[0] if '(detected)' in s else s for s in autorandr_all]
    options = [f"Load <tt>{s}</tt>" for s in configurations]
    # options must not point to the same list as configurations.

    def add_special_option(name):
        options.append(name)
        return len(options) - 1

    idx_common = add_special_option("Clone common")# + subtext("Clone all outputs at common resolution"))
    idx_clone_largest = add_special_option("Clone largest")# + subtext("Clone all outputs at largest resolution"))
    idx_horizontal = add_special_option("Arrange horizontally")# + subtext("Arrange outputs horizontally"))
    idx_vertical = add_special_option("Arrange vertically")# + subtext("Arrange outputs vertically"))

    idx_arandr = add_special_option("Custom" + subtext("ARandR"))

    if not only_detected:
        for cfg in autorandr_detected:
            options[configurations.index(cfg)] += subtext('Detected')

    try:
        autorandr_active = [s.strip() for s in autorandr('--current').splitlines()]
        for cfg in autorandr_active:
            options[configurations.index(cfg)] += subtext('Current')
        idx_save = None
    except:
        idx_save = add_special_option("Save current")

    idx_dir = add_special_option("View all" + subtext("Open AutoRandR directory in terminal"))

    selected = rofi(options, '-no-custom', '-markup-rows', p="AutoRandR", format='i')

    if selected < len(autorandr_detected):
        autorandr('-l', autorandr_detected[selected])
    elif selected == idx_arandr:
        call(['arandr'])
    elif selected == idx_save:
        new_name = rofi(None, p="AutoRandR config name").strip()
        autorandr('-s', new_name)
    elif selected == idx_dir:
        import os
        config_home = os.path.expanduser(os.environ.get('XDG_CONFIG_HOME', '~/.config'))
        config_dir = os.path.join(config_home, 'autorandr')
        call(['rofi-sensible-terminal'], cwd=config_dir)

show_autorandrofi()
