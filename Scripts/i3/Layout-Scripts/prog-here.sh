#!/bin/bash

i3 "move container to workspace $(basename $(pwd)); workspace $(basename $(pwd)); layout tabbed; split v; layout stacked"
xtoolwait subl3 -n .
xtoolwait alacritty
i3 "focus up"
xtoolwait firefox --new-window
i3 "move container right; focus left"

clear
