#!/bin/bash

#                                 QW  CO
xmodmap -e "keycode 25 = space" # w   w
xmodmap -e "keycode 38 = Left"  # a   a
xmodmap -e "keycode 39 = Down"  # s   r
xmodmap -e "keycode 40 = Right" # d   s
xmodmap -e "keycode 44 = z"     # j   n
xmodmap -e "keycode 45 = x"     # k   e
xmodmap -e "keycode 47 = c"     # ;   o

# # Reverse mappings to make i3wm happy
# # (assumes Colemak)
# xmodmap -e "keycode 65 = w"
# xmodmap -e "keycode 113 = a"
# xmodmap -e "keycode 116 = r"
# xmodmap -e "keycode 114 = s"
# xmodmap -e "keycode 52 = n"
# xmodmap -e "keycode 53 = e"
# xmodmap -e "keycode 54 = o"

i3-msg reload
