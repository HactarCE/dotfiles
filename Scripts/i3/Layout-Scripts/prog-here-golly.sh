#!/bin/bash

i3 "move container to workspace $(basename $(pwd)); workspace $(basename $(pwd)); layout tabbed; split v; layout stacked"
xtoolwait subl3 -n .
xtoolwait alacritty -d ~/.golly/Rules
i3 "focus up"
xtoolwait golly
i3 "move container left; focus right"
xtoolwait firefox --new-window http://golly.sourceforge.net/Help/index.html
i3 "move container right; focus left"

clear
