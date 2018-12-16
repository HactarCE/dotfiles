#!/bin/bash

if pgrep polybar; then

    while read pid; do
        polybar-msg -p "$pid" cmd quit
    done </var/run/user/$(id -u)/polybar-top.pid

    while read pid; do
        polybar-msg -p "$pid" cmd quit
    done </var/run/user/$(id -u)/polybar-bottom.pid

else
    ~/.config/polybar/launch.py
fi
