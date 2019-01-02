#!/bin/bash

case "$1" in
    --toggle)
        if [ "$(pgrep -x compton)" ]; then
            pkill -x compton
        else
            compton -b
        fi
        ;;
    *)
        if [ "$(pgrep -x compton)" ]; then
            echo ""
        else
            echo ""
        fi
        ;;
esac
