#!/bin/bash

mkdir -p ~/.config/dconf/user.d
cd ~/.config/dconf/user.d

dconf dump /org/xfce/mousepad/preferences/ > mousepad
