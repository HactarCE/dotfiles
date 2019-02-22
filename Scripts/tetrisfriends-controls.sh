#!/bin/bash

#                                 QW  CO
xmodmap -e "keycode 25 = space" # w   w
xmodmap -e "keycode 38 = Left"  # a   a
xmodmap -e "keycode 39 = Down"  # s   r
xmodmap -e "keycode 40 = Right" # d   s
xmodmap -e "keycode 44 = z"     # j   n
xmodmap -e "keycode 45 = x"     # k   e
xmodmap -e "keycode 47 = c"     # ;   o

i3-msg reload
