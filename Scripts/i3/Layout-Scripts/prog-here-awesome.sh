#!/bin/bash

cd ~/.config/awesome || cd ~/Dropbox/Awesome-WM

i3 "move container to workspace $(basename $(pwd)); workspace $(basename $(pwd)); layout tabbed; split v; layout stacked"
xtoolwait subl3 -n . rc.lua
xtoolwait google-chrome-stable --new-window https://www.lua.org/pil/1.html https://awesomewm.org/doc/
i3 "move container right; focus left"

clear
