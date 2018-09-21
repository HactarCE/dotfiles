#!/bin/sh

pacmd stat | grep 'Default sink' | grep -q bluez && echo ""

