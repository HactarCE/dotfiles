#!/bin/bash

i3 "move container to workspace YAY; workspace YAY; layout tabbed; split v; layout stacked"
xtoolwait subl -n ~/Dropbox/wip.txt
i3 "focus up"
xtoolwait google-chrome-stable --new-window https://www.archlinux.org/news/
i3 "move container right; focus left"

clear
