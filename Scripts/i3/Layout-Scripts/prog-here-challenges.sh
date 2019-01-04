#!/bin/bash

i3 "move container to workspace $(basename $(pwd)); workspace $(basename $(pwd)); layout tabbed; split v; layout stacked"
xtoolwait subl3 -n .
xtoolwait termite -e "zsh -c 'while true; do python; clear; done'" -t python
i3 "split h; layout tabbed"
xtoolwait termite -e "zsh -c 'while true; do clj; clear; done'" -t clj
i3 "focus left; focus up"
xtoolwait google-chrome-stable --new-window
i3 "move container left; focus right"
xtoolwait google-chrome-stable --new-window https://docs.python.org/3/ https://clojure.org/api/api
i3 "move container right; focus left"

clear
