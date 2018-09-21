#!/usr/bin/sh

STATUS_FILE="$HOME/.config/pianobar/status"
OFFLINE_MSG="Pianobar is offline."

while true; do
    while [ -f "$STATUS_FILE" ]; do
        sleep 0.2
        cat "$STATUS_FILE"
        pkill -0 pianobar || rm "$STATUS_FILE"
    done
    echo "$OFFLINE_MSG"
    while [ ! -f "$STATUS_FILE" ]; do
        sleep 2
        # inotifywait -qqt 2 -e create "$(dirname $STATUS_FILE)"
    done
done
