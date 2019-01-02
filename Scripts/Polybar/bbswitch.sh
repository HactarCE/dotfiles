#!/bin/bash

if [ -f /proc/acpi/bbswitch ]; then

    case "$1" in
        --toggle)
            if grep -q ON /proc/acpi/bbswitch; then
                tee /proc/acpi/bbswitch <<<OFF
            else
                tee /proc/acpi/bbswitch <<<ON
            fi
            ;;
        *)
            if grep -q ON /proc/acpi/bbswitch; then
                echo -n "Nvidia GPU"
            else
                echo -n "Intel GPU"
            fi
            if systemctl is-active bumblebeed.service | grep -q inactive; then
                echo
            else
                echo " (auto)"
            fi
            ;;
    esac

fi
