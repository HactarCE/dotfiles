#!/bin/bash

# KEYBOARD
xset r rate 200 35
setxkbmap -option caps:backs
xmodmap -e "clear Lock"

# MOUSE
ids=$(xinput --list | awk -v search="Logitech Gaming Mouse G600" \
    '$0 ~ search {match($0, /id=[0-9]+/);\
                  if (RSTART) \
                    print substr($0, RSTART+3, RLENGTH-3)\
                 }'\
     )
for i in $ids; do
    xinput set-prop $i 'libinput Accel Speed' -0.5
done
