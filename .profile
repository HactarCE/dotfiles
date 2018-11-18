#
# ~/.profile
#
#

[[ "$XDG_CURRENT_DESKTOP" == "KDE" ]] || export QT_QPA_PLATFORMTHEME="qt5ct"

[[ -f ~/.extend.profile ]] && . ~/.extend.profile

export PATH=$PATH":$HOME/.local/bin"

export BROWSER=/usr/bin/vivaldi-stable
export EDITOR="subl -nw"
export SHELL=/bin/zsh
export TERMINAL=termite

export DMENU_SETTINGS='-i -h 20 -fn "xos4 Terminus-12" -nb "#000" -nf "#fff" -sb "#0070da" -sf "#fff" -dim 0.4'

# NVIDIA cache
export __GL_SHADER_DISK_CACHE_PATH="$HOME/.cache/nv/GLCache"

# Zsh autocomplete cache
export ANTIGEN_COMPDUMPFILE="$HOME/.cache/zcompdump"

# Wine settings
export WINEARCH=win64
export WINEPREFIX="$HOME/.wine"

# # Hold CapsLock for Control, or tap for Escape
# # Hold Tab for Super, or tap for Tab
# xmodmap -e "keycode 23 = Super_L"
# xmodmap -e "keycode any = Tab ISO_Left_Tab Tab ISO_Left_Tab"
# setxkbmap -option caps:ctrl
# xcape -e "Super_L=Tab;Control_L=Escape"

# xmodmap -e "keycode 23 = Control_L NoSymbol Control_L"
# xcape -e "Super_L=Escape"
