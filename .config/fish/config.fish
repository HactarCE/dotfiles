set -p PATH /opt/homebrew/bin
set -p PATH /Users/andrew/.cargo/bin
set -p PATH /Users/andrew/.local/bin

set -gx TERMINAL wezterm
set -gx EDITOR code -w
set -gx HOSTNAME eigenvoid

# PFETCH CONFIG
set -gx PF_INFO title os kernel pkgs memory shell editor
set -gx PF_COL1 4
set -gx PF_COL2 3
set -gx PF_COL3 1

set fzf_preview_dir_cmd exa --all --color=always
fzf_configure_bindings --directory=\cf
starship init fish | source
zoxide init fish | source

# SAFETY
alias cp='cp -iR'
alias sucp='sudo cp -iR'
alias mv='mv -i'
alias sumv='sudo mv -i'
alias rmm='/bin/rm -i'
alias rm="echo 'Use either del=\"trash\" or rmm=\"rm -i\"'; :"
alias del='trash'
alias surmm='sudo rm -i'
alias sudel='sudo trash'

# LS
alias ls='exa'
alias ll='ls --long --git'
alias l='ll'
alias la='ll --all'
alias tree='exa --tree'
alias lt='ll --tree'
alias lta='lt --all'
alias ltl='lt -L'
alias ltal='lta -L'

# OXIDIZED COREUTILS
alias cat='bat'
alias du='dust -s'

# CARGO
alias c='cargo'
alias cb='cargo build'
alias cbr='cargo build --release'
alias cr='cargo run'
alias crr='cargo run --release'
alias ct='cargo test'
alias ctr='cargo test --release'
alias cch='cargo check'
function cargo-expand
    cargo expand $argv | bat -l rust
end

# DOT DOT DOT
alias ...='cd ../..'
alias ....='cd ../../..'
alias .....='cd ../../../..'
alias ......='cd ../../../../..'
alias .......='cd ../../../../../..'

# GUI APPS
alias a='open -a'
alias ff='firefox'
alias ffnt='firefox --new-tab'
alias ffnw='firefox --new-window'
alias f='open -a Finder .'
alias o='open'


# MISC
alias cls='clear'
alias cx='chmod +x'
alias c-x='chmod -x'
alias fn='functions'
alias jj='java -jar'
alias suno='sudo nano'
alias md='mkdir -p'
alias rg='rg -S' # smart case
alias sus='sudo -s'
alias tb='nc termbin.com 9999'
alias u='unp -U'
alias q='exit'
alias zo='zoxide'

function echo-dots
    for i in $argv
        tput setaf $i
        echo -n '● '
    end
    echo
end

function pf
    pfetch
    echo-dots 1 5 4 6 2 3 8 15 7 0
    # echo-dots 9 13 12 14 10 11
end

function fish_greeting
    pf
end
