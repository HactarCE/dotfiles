set -p PATH /opt/homebrew/bin
set -p PATH /Users/andrew/.cargo/bin
set -p PATH /Users/andrew/.local/bin

set -gx TERMINAL wezterm
set -gx EDITOR code -w
set -gx HOSTNAME eigenvoid

# PFETCH CONFIG
set -gx PF_INFO title os kernel shell
set -gx PF_COL1 4
set -gx PF_COL2 3
set -gx PF_COL3 1

set fzf_preview_dir_cmd eza --all --color=always
fzf_configure_bindings --directory=\cf
starship init fish | source
zoxide init fish --cmd c | source
zellij setup --generate-completion fish | source

# DOT DOT DOT
abbr ...        'cd ../..'
abbr ....       'cd ../../..'
abbr .....      'cd ../../../..'
abbr ......     'cd ../../../../..'
abbr .......    'cd ../../../../../..'
abbr ........   'cd ../../../../../../..'
abbr .........  'cd ../../../../../../../..'

# BREW
abbr b          brew
abbr 'b?'       'brew info'
abbr bc         'brew cleanup'
abbr bi         'brew install'
abbr bl         'brew list'
abbr bre        'brew reinstall'
abbr bs         'brew search'
abbr bu         'brew uninstall'
abbr bup        'brew upgrade'
abbr bo         'brew outdated'

# CARGO
abbr co         cargo
abbr cb         'cargo build'
abbr cbr        'cargo build --release'
abbr cr         'cargo run'
abbr crr        'cargo run --release'
abbr ct         'cargo test'
abbr ctr        'cargo test --release'
abbr cch        'cargo check'
abbr --set-cursor cmx 'cargo expand % | bat -l rust'

# GITHUB
abbr ghr        'gh repo'
abbr ghrc       'gh repo clone'

# LS / EXA
alias ls 'eza --git'
abbr ll         'ls -l'
abbr l          'ls -l'
abbr la         'ls -la'
abbr tree       'ls -T'
abbr lt         'ls -lT'
abbr lta        'ls -lTa'
abbr ltl        'ls -lTL'
abbr ltal       'ls -lTaL'

# PYTHON
abbr py2        python2
abbr py3        python3
abbr py         python3
abbr supy2      'sudo python2'
abbr supy3      'sudo python3'
abbr supy       'sudo python'
abbr pi2        'pip2 install --user'
abbr pi3        'pip3 install --user'
abbr pi         'pip install --user'
abbr pie2       'pi2 -e'
abbr pie3       'pi3 -e'
abbr pie        'pi -e'
abbr venv       'python -m venv'

# ZELLIJ
abbr z          zellij
abbr za         'zellij attach'
abbr ze         'zellij edit'
abbr zef        'zellij edit --floating'
abbr zk         'zellij kill-session'
abbr zka        'zellij kill-all-sessions'
abbr zl         'zellij list-sessions'

# GUI APPS
abbr a          'open -a'
abbr ff         firefox
abbr ffnt       'firefox --new-tab'
abbr ffnw       'firefox --new-window'
abbr f          'open -a Finder .'
abbr o          open

# SAFETY
abbr cp         'cp -iR'
abbr sucp       'sudo cp -iR'
abbr mv         'mv -i'
abbr sumv       'sudo mv -i'
abbr rmm        '/bin/rm -i'
alias rm "echo \"Use either del='trash' or rmm='rm -i'\"; :"
abbr del        trash
abbr surmm      'sudo rm -i'
abbr sudel      'sudo trash'

# MISC
abbr cat        bat
abbr cl         clear
abbr cls        clear
abbr cx         'chmod +x'
abbr c-         x 'chmod -x'
abbr du         'dust -s'
abbr fn         functions
abbr i          insect
abbr jj         'java -jar'
abbr ln         'ln -s' # symbolic link
abbr md         'mkdir -p'
abbr q          exit
abbr rg         'rg -S' # smart case
abbr suno       'sudo nano'
abbr sus        'sudo -s'
abbr tb         'nc termbin.com 9999'
abbr unp        'unp -U'
abbr zx         zoxide

alias dot '/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'

function echo-dots --description "Draw dots with some colors"
    for i in $argv
        tput setaf $i
        echo -n '● '
    end
    echo
end

function pf --description "Run pfetch and draw some colored dots"
    pfetch
    echo-dots 1 5 4 6 2 3 8 15 7 0
    # echo-dots 9 13 12 14 10 11
end

function fish_greeting
    pf
end
