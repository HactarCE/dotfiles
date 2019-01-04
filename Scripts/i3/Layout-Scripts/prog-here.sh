#!/bin/bash

i3 "move container to workspace $(basename $(pwd)); workspace $(basename $(pwd)); layout tabbed; split v; layout stacked"
xtoolwait subl3 -n .
xtoolwait termite
i3 "focus up"
xtoolwait google-chrome-stable --new-window
i3 "move container right; focus left"

clear
