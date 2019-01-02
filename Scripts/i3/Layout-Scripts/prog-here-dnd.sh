#!/bin/bash

cd ~/Dropbox/Games/Dungeons-and-Dragons/
i3 "move container to workspace D&D; workspace D&D; layout stacked"
xtoolwait termite .
i3 "move up; focus down"
xtoolwait subl -n . ./*/*.txt
i3 "focus up"
xtoolwait google-chrome-stable --new-window https://twinelab.net/spellbook/ https://roll20.net/compendium/dnd5e/Items%20List#content ./*.pdf
i3 "move container right; focus left"
xdotool getactivewindow windowkill
