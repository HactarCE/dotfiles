#!/bin/bash

id=$(xdotool getactivewindow)

if [[ "$(xdotool getactivewindow getwindowname)" = "Steam" && "$(xprop -id $id WM_CLASS | cut -d= -f2 | xargs)" = "Steam, Steam" ]]; then
    # echo yes steam
    xdotool getactivewindow windowunmap
else
    # echo no steam
    wmctrl -c :ACTIVE:
fi
