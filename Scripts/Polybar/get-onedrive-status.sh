#!/usr/bin/bash

onedrive_output=$(timeout 5 onedrive --display-sync-status 2>&1 || echo TIMEOUT)

echo_remaining() {
    case "$onedrive_output" in
        # display data remaining to transfer
        (*:*)   echo " ${onedrive_output##*: }";;
        (*)     echo;;
    esac
}

if [[ "$onedrive_output" == "TIMEOUT" ]]; then
    # command timed out
    echo '?'
elif ps aux | grep -v "$0" | grep -v grep | grep -q onedrive; then
    if echo "$onedrive_output" | grep -qi 'cannot connect'; then
        # no connection
        echo 
    elif echo "$onedrive_output" | grep -q 'in sync'; then
        # in sync
        echo -n 
        echo_remaining
    else
        # syncing
        echo -n 痢
        echo_remaining
    fi
else
    # disabled
    echo 
fi
