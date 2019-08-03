#!/usr/bin/bash

xclip -selection clipboard -t image/png
notify-send "Screenshot copied to clipboard"
