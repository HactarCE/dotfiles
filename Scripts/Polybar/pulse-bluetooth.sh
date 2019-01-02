#!/bin/bash

pacmd stat | grep 'Default sink' | grep -q bluez && echo ""
