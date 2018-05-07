#!/bin/sh

while true; do
  ~/Scripts/fix-usbs.sh
  watch -g lsusb
  sleep 3
done
