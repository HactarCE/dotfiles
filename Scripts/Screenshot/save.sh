#!/usr/bin/bash

filename=$(date +"/tmp/screenshot_%Y-%m-%d_%H:%M:%S.png")
tee > "$filename"
notify-send "Screenshot saved to $filename"
