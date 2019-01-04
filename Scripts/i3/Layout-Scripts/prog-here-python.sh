#!/bin/bash

i3 "move container to workspace $(basename $(pwd)); workspace $(basename $(pwd)); layout tabbed; split v; layout stacked"
xtoolwait subl3 -n .
xtoolwait termite -e "zsh -c 'while true; do python; clear; done'" -t python
i3 "focus up"
xtoolwait google-chrome-stable --new-window https://docs.python.org/3/
i3 "move container right; focus left"

clear
