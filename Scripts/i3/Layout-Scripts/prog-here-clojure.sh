#!/bin/bash

i3 "move container to workspace $(basename $(pwd)); workspace $(basename $(pwd)); layout tabbed; split v; layout stacked"
xtoolwait subl3 -n .
xtoolwait alacritty -e "zsh -c 'while true; do clj; clear; done'" -t clj
i3 "focus up"
xtoolwait google-chrome-stable --new-window http://localhost:3000/
i3 "move container left; focus right"
xtoolwait google-chrome-stable --new-window https://clojure.org/api/api
i3 "move container right; focus left"

clear
