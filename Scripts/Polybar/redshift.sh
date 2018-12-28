#!/bin/sh

case "$1" in
    --toggle)
        if [ "$(pgrep -x redshift)" ]; then
            pkill -x redshift
        else
            i3 'exec redshift'
        fi
        ;;
    *)
        if [ "$(pgrep -x redshift)" ]; then
            echo ""
        else
            echo ""
        fi
        ;;
esac
