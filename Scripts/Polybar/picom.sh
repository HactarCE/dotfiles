#!/bin/bash

case "$1" in
    --toggle)
        if [ "$(pgrep -x picom)" ]; then
            pkill -x picom
        else
            picom -b
        fi
        ;;
    *)
        if [ "$(pgrep -x picom)" ]; then
            echo ""
        else
            echo ""
        fi
        ;;
esac
