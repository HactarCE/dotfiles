#!/bin/sh

# while true; do
    if setxkbmap -query | grep 'variant:' >/dev/null; then
        variant=$(setxkbmap -query | grep variant | cut -d: -f2)
        variant=$(echo $variant) # kill extaneous whitespace
        echo "${variant^}" # capitalize first letter
    else
        echo " Qwerty"
    fi
#     watch -gn 0.2 setxkbmap -query &>/dev/null
# done
