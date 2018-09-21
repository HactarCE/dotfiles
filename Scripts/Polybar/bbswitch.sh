#!/bin/sh

case "$1" in
    --toggle)
        if grep-q ON /proc/acpi/bbswitch; then
            tee /proc/acpi/bbswitch <<< OFF
        else
            tee /proc/acpi/bbswitch <<< ON
        fi
        ;;
    *)
        if grep -q ON /proc/acpi/bbswitch; then
            echo "Nvidia GPU"
        else
            echo "Intel GPU"
        fi
        ;;
esac
