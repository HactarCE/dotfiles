#!/usr/bin/bash

onedrive_output=$(onedrive --display-sync-status)

if ps aux | grep -v "$0" | grep -v grep | grep -q onedrive; then
    if echo "$onedrive_output" | grep -q 'in sync'; then
        # in sync
        echo 
    else
        # syncing
        case "$onedrive_output" in
            # display data remaining to transfer
            (*:*)   echo 痢 "${onedrive_output##*: }";;
            # just show icon
            (*)     echo 痢;;
        esac
    fi
else
    # disabled
    echo 
fi
