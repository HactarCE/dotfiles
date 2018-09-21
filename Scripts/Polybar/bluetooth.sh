#!/bin/sh

btcontroller="$(bluetoothctl list | head -n1 | cut -d' ' -f2)"
btstatus="$(bluetoothctl show $btcontroller | grep Powered | cut -d':' -f2 | cut -c2-)"

case "$1" in
    --toggle)
        if [ "$btstatus" = "yes" ]; then
            bluetoothctl power off
        else
            bluetoothctl power on
        fi
        ;;
    *)
        if [ "$btstatus" = "yes" ]; then
            if pacmd stat | grep 'Default sink' | grep -q bluez; then
                echo ""
            else
	              echo ""
            fi
        else
	          echo ""
        fi
        ;;
esac
