#
# ~/.profile
#
#

[[ "$XDG_CURRENT_DESKTOP" == "KDE" ]] || export QT_QPA_PLATFORMTHEME="qt5ct"

[[ -f ~/.extend.profile ]] && . ~/.extend.profile

export PATH=$PATH":$HOME/.local/bin"

export BROWSER=/usr/bin/google-chrome-stable
export EDITOR="subl3 -nw"
export SHELL=/bin/zsh
export TERMINAL=alacritty

# NVIDIA cache
export __GL_SHADER_DISK_CACHE_PATH="$HOME/.cache/nv/GLCache"

# Zsh autocomplete cache
export ANTIGEN_COMPDUMPFILE="$HOME/.cache/zcompdump"

# Wine settings
export WINEARCH=win64
export WINEPREFIX="$HOME/.wine"

# GTK Theme
export GTK2_RC_FILES="$HOME/.gtkrc-2.0"

# Keyboard settings for Wayland
XKB_DEFAULT_VARIANT=colemak
XKB_DEFAULT_OPTIONS=shift:both_capslock

# # Hold CapsLock for Control, or tap for Escape
# # Hold Tab for Super, or tap for Tab
# xmodmap -e "keycode 23 = Super_L"
# xmodmap -e "keycode any = Tab ISO_Left_Tab Tab ISO_Left_Tab"
# setxkbmap -option caps:ctrl
# xcape -e "Super_L=Tab;Control_L=Escape"

# xmodmap -e "keycode 23 = Control_L NoSymbol Control_L"
# xcape -e "Super_L=Escape"
