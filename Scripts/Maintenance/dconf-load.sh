#!/bin/bash

cat ~/.config/dconf/user.d/* | dconf load /
