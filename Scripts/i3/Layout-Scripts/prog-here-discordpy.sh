#!/bin/bash

i3 "move container to workspace $(basename $(pwd)); workspace $(basename $(pwd)); layout tabbed; split v; layout stacked"
xtoolwait subl3 -n .
xtoolwait alacritty -e "zsh -c 'while true; do python; clear; done'" -t python
i3 "focus up"
xtoolwait google-chrome-stable --new-window https://discordpy.readthedocs.io/en/stable/api.html https://discordpy.readthedocs.io/en/stable/ext/commands/api.html
i3 "move container right; focus left"

clear
