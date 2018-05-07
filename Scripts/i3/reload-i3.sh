#!/usr/bin/sh

i3-msg reload | grep -i true && notify-send Reloaded i3
