#!/bin/bash

i3 "move container to workspace $(basename $(pwd)); workspace $(basename $(pwd)); layout tabbed; split v; layout stacked"
xtoolwait subl3 -n .
xtoolwait alacritty -t python -e zsh -c 'while true; do python; clear; done'
i3 "focus up"
xtoolwait firefox --new-window https://docs.python.org/3/
i3 "move container right; focus left"

clear
