export DEFAULT_USER="andy"
export TERM="xterm-256color"
export ZSH=/home/${DEFAULT_USER}/.oh-my-zsh
export LANG="en_US.UTF-8"

HYPHEN_INSENSITIVE="true"
COMPLETION_WAITING_DOTS="true"
# /!\ do not use with zsh-autosuggestions

plugins=(k tig gitfast colored-man-pages colorize command-not-found cp dirhistory autojump zsh-completions fast-syntax-highlighting zsh-autosuggestions)
# /!\ zsh-syntax-highlighting and then zsh-autosuggestions must be at the end

source $ZSH/oh-my-zsh.sh
# source /usr/share/zsh/plugins/fast-syntax-highlighting/fast-syntax-highlighting.plugin.zsh
autoload -U promptinit; promptinit
prompt pure
PROMPT='%(?.%F{02}.%F{01})%B»%f%b '

# The defaults for these are practically unreadable, so set them to be the same as normal directories
# TODO: doesn't work in tab completion
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


rule () {
	print -Pn '%F{blue}'
	local columns=$(tput cols)
	for ((i=1; i<=columns; i++)); do
	   printf "\u2588"
	done
	print -P '%f'
}

function _my_clear() {
	echo
	rule
	zle clear-screen
}
zle -N _my_clear
bindkey '^l' _my_clear

bindkey '^ ' autosuggest-accept

if [ -f ~/.zsh_aliases ]; then
    . ~/.zsh_aliases
fi
