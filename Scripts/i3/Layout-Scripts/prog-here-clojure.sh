#!/bin/bash

i3 "move container to workspace $(basename $(pwd)); workspace $(basename $(pwd)); layout tabbed; split v; layout stacked"
xtoolwait subl3 -n .
xtoolwait alacritty -t clj -e zsh -c 'while true; do clj; clear; done'
i3 "focus up"
xtoolwait firefox --new-window http://localhost:3000/
i3 "move container left; focus right"
xtoolwait firefox --new-window https://clojure.org/api/api
i3 "move container right; focus left"

clear
