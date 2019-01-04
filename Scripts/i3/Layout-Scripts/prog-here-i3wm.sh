#!/bin/bash

cd ~/.config/i3

i3 "move container to workspace $(basename $(pwd)); workspace $(basename $(pwd)); layout tabbed; split v; layout stacked"
xtoolwait subl3 -n . config
xtoolwait google-chrome-stable --new-window https://i3wm.org/docs/userguide.html
i3 "move container right; focus left"

clear
