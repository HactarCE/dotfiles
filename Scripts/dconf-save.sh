#!/bin/bash

mkdir -p ~/.config/dconf/user.d
cd ~/.config/dconf/user.d

rm -rf ~/.config/dconf/user.d/*
dconf dump / > tmp-dump

crudini --get --format=ini tmp-dump 'org/xfce/mousepad/preferences/view' >> mousepad
echo >> mousepad
crudini --get --format=ini tmp-dump 'org/xfce/mousepad/preferences/window' >> mousepad

rm ~/.config/dconf/user.d/tmp-dump
