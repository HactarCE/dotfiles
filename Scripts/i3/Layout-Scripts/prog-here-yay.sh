#!/bin/bash

i3 "move container to workspace YAY; workspace YAY; layout tabbed; split v; layout stacked"
xtoolwait subl3 -n ~/Dropbox/wip.txt
i3 "focus up"
xtoolwait firefox --new-window https://www.archlinux.org/news/
i3 "move container right; focus left"

clear
