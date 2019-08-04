#!/bin/bash

cd ~/.config/sublime-text-3/Packages/Hactar

i3 "move container to workspace $(basename $(pwd)); workspace $(basename $(pwd)); layout tabbed; split v; layout stacked"
xtoolwait subl3 -n .
xtoolwait alacritty -t python -e zsh -c 'while true; do python; clear; done'
i3 "focus up"
xtoolwait google-chrome-stable --new-window https://www.sublimetext.com/docs/3/
i3 "move container right; focus left"

clear
