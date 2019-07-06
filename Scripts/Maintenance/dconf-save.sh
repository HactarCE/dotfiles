#!/bin/bash

mkdir -p ~/.config/dconf/user.d
cd ~/.config/dconf/user.d

rm -rf ~/.config/dconf/user.d/*
dconf dump / > tmp-dump

crudini --get --format=ini tmp-dump 'org/xfce/mousepad/preferences/view' >> mousepad
echo >> mousepad
crudini --get --format=ini tmp-dump 'org/xfce/mousepad/preferences/window' >> mousepad

crudini --get --format=ini tmp-dump 'org/nemo/preferences' >> nemo
echo >> nemo
crudini --get --format=ini tmp-dump 'org/nemo/plugins' >> nemo
echo >> nemo
crudini --get --format=ini tmp-dump 'org/nemo/sidebar-panels/tree' >> nemo

crudini --get --format=ini tmp-dump 'org/onboard' >> onboard
echo >> onboard
crudini --get --format=ini tmp-dump 'org/onboard/keyboard' >> onboard
echo >> onboard
crudini --get --format=ini tmp-dump 'org/onboard/theme-settings' >> onboard

rm ~/.config/dconf/user.d/tmp-dump
