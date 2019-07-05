export LANG=en_US.UTF-8
export TERM=xterm-256color
export ZSH=~/.antigen/bundles/robbyrussell/oh-my-zsh

source ~/.antigen/antigen.zsh

antigen use oh-my-zsh



################################
# SPACESHIP PROMPT SETTINGS
################################


SPACESHIP_PROMPT_ORDER=(
  dir           # Current directory section
  git           # Git section (git_branch + git_status)
  venv          # virtualenv section
  conda         # conda virtualenv section
  pyenv         # Pyenv section
  exec_time     # Execution time
  line_sep      # Line break
  user          # Username section
  host          # Hostname section
  vi_mode       # Vi-mode indicator
  jobs          # Background jobs indicator
  exit_code     # Exit code section
  char          # Prompt character
)

SPACESHIP_PROMPT_DIR_PREFIX=''

SPACESHIP_PROMPT_DEFAULT_PREFIX='with'
SPACESHIP_CHAR_SYMBOL='»'
SPACESHIP_CHAR_SYMBOL_ROOT='#'
SPACESHIP_CHAR_SYMBOL_SECONDARY='… '
SPACESHIP_CHAR_SUFFIX=' '
SPACESHIP_DIR_TRUNC_PREFIX='…/'
SPACESHIP_DIR_TRUNC=0

SPACESHIP_USER_PREFIX=''
SPACESHIP_HOST_PREFIX='\x08@'

# VENV
SPACESHIP_VENV_PREFIX='venv:('
SPACESHIP_VENV_SUFFIX=') '

# CONDA
SPACESHIP_CONDA_PREFIX='conda:('
SPACESHIP_CONDA_SUFFIX=') '
SPACESHIP_CONDA_SYMBOL=''

# PYENV
SPACESHIP_PYENV_PREFIX='pyenv:('
SPACESHIP_PYENV_SUFFIX=') '
SPACESHIP_PYENV_SYMBOL=''



################################
# ZSH OPTIONS
################################


# http://zsh.sourceforge.net/Doc/Release/Options.html

# Changing Directories
setopt auto_cd auto_pushd pushd_ignore_dups

# Completion
setopt always_to_end complete_in_word list_packed

# Expansion and Globbing
setopt glob_star_short

# History
setopt extended_history hist_expire_dups_first hist_find_no_dups hist_ignore_dups hist_ignore_space hist_verify share_history
unsetopt bang_hist
export HISTFILE=~/.zsh_history
export HISTSIZE=100000
export SAVEHIST=$HISTSIZE

# Input/Output
setopt ignore_eof interactive_comments sun_keyboard_hack
unsetopt flow_control
export KEYBOARD_HACK="'"

# Shell State
setopt interactive

# Zle
unsetopt beep



################################
# ANTIGEN PLUGINS
################################


antigen theme https://github.com/denysdovhan/spaceship-zsh-theme spaceship


# https://github.com/robbyrussell/oh-my-zsh/wiki/Plugins-Overview

### Completions
# antigen bundle autopep8
antigen bundle gitfast
# antigen bundle pep8
antigen bundle pip
# antigen bundle pyenv
antigen bundle python

### Aliases
# antigen bundle common-aliases
antigen bundle cp
antigen bundle git
antigen bundle history
antigen bundle python
antigen bundle rsync

### Cosmetic
antigen bundle colored-man-pages

### Movement
antigen bundle autojump
# # dirhistory has more features (and nicer keybinds), but dircycle doesn't
# # replace the prompt, so I keep both.
# antigen bundle dircycle
antigen bundle dirhistory

### Miscellaneous
antigen bundle colemak
antigen bundle command-not-found
antigen bundle gitignore
antigen bundle zdharma/fast-syntax-highlighting
antigen bundle zsh-users/zsh-autosuggestions

antigen apply

# Workaround https://github.com/robbyrussell/oh-my-zsh/issues/5765
spaceship_prompt_first_line() { print -rP "$(spaceship_prompt | head -n -1)" }
add-zsh-hook precmd spaceship_prompt_first_line
export PROMPT='$(spaceship_prompt | tail -n 1)'

if [ -f ~/.zsh_aliases ]; then
    . ~/.zsh_aliases
fi



################################
# MISCELLANEOUS
################################


# The default colors for other-writable and sticky files/directories have very
# little foreground/background contrast and so are practically unreadable; set
# them to be the same as normal directories.
LS_COLORS="${LS_COLORS:s/ow=34;42/ow=01;34}"
LS_COLORS="${LS_COLORS:s/tw=37;44/tw=01;34}"


FAST_HIGHLIGHT_HIGHLIGHTERS=(main brackets pattern cursor)
FAST_HIGHLIGHT_STYLES[cursor]='bold'

FAST_HIGHLIGHT_STYLES[alias]='fg=blue,bold'
FAST_HIGHLIGHT_STYLES[suffix-alias]='fg=blue,bold'
FAST_HIGHLIGHT_STYLES[builtin]='fg=green,bold'
FAST_HIGHLIGHT_STYLES[function]='fg=green,bold'
FAST_HIGHLIGHT_STYLES[command]='fg=green,bold'
FAST_HIGHLIGHT_STYLES[precommand]='fg=green,bold'
FAST_HIGHLIGHT_STYLES[hashed-command]='fg=green,bold'


ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=7'
ZSH_AUTOSUGGEST_USE_ASYNC='true'

HYPHEN_INSENSITIVE='true'
COMPLETION_WAITING_DOTS='true'


rule () {
	print -Pn '%F{blue}'
	local columns=$(tput cols)
	for ((i=1; i<=columns; i++)); do
	   printf '\u2588'
	done
	print -P '%f'
}

function _zle_clear() {
	echo
	rule
	zle clear-screen
}

zle -N _zle_clear
bindkey '^l' _zle_clear
bindkey '^ ' autosuggest-accept
bindkey -s '^x' '^l^p^j'

# Bind shift+arrow to the same as arrow
bindkey -s '^[[1;2A' '^[OA'
bindkey -s '^[[1;2B' '^[OB'
bindkey -s '^[[1;2C' '^[OC'
bindkey -s '^[[1;2D' '^[OD'
