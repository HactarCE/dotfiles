#!/bin/bash

i3 "move container to workspace $(basename $(pwd)); workspace $(basename $(pwd)); layout tabbed; split v; layout stacked"
xtoolwait subl3 -n .
xtoolwait alacritty -t python -e zsh -c 'while true; do python; clear; done'
i3 "split h; layout tabbed"
xtoolwait alacritty -t clj -e zsh -c 'while true; do clj; clear; done'
i3 "focus left; focus up"
xtoolwait firefox --new-window
i3 "move container left; focus right"
xtoolwait firefox --new-window https://docs.python.org/3/ https://clojure.org/api/api
i3 "move container right; focus left"

clear
