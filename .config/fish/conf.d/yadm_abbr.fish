#!/usr/bin/env fish
#
# yadm-abbr: yadm abbreviations for the fish shell

abbr y 'yadm'

abbr ya 'yadm add'
abbr yaa 'yadm add --all'
abbr yapa 'yadm add --patch'
abbr yau 'yadm add --update'
abbr yav 'yadm add --verbose'
abbr yap 'yadm apply'
abbr yapt 'yadm apply --3way'

abbr yb 'yadm branch'
abbr yba 'yadm branch -a'
abbr ybd 'yadm branch -d'
abbr ybdf 'yadm branch -d -f'
abbr ybD 'yadm branch -D'
abbr ybDf 'yadm branch -D -f'
abbr ybnm 'yadm branch --no-merged'
abbr ybr 'yadm branch --remote'

abbr ybl 'yadm blame -b -w'

abbr ybs 'yadm bisect'
abbr ybsb 'yadm bisect bad'
abbr ybsg 'yadm bisect good'
abbr ybsr 'yadm bisect reset'
abbr ybss 'yadm bisect start'

abbr yc 'yadm commit -v'
abbr yci 'yadm commit --allow-empty -v -m\'chore: initial commit\''
abbr yc! 'yadm commit -v --amend'
abbr ycn 'yadm commit -v --no-edit'
abbr ycn! 'yadm commit -v --amend --no-edit'
abbr yca 'yadm commit -a -v'
abbr yca! 'yadm commit -a -v --amend'
abbr ycan! 'yadm commit -a -v --no-edit --amend'
abbr ycans! 'yadm commit -a -v -s --no-edit --amend'
abbr ycam 'yadm commit -a -m'
abbr ycas 'yadm commit -a -s'
abbr ycasm 'yadm commit -a -s -m'
abbr ycsm 'yadm commit -s -m'
abbr ycm 'yadm commit -m'
abbr ycs 'yadm commit -S'

abbr ycf 'yadm config --list'

abbr ycl 'yadm clone --recurse-submodules'

abbr yclean 'yadm clean -id'

abbr yco 'yadm checkout'
abbr ycob 'yadm checkout -b'
abbr ycom 'yadm checkout main'
abbr ycoh 'yadm checkout hotfix/'
abbr ycor 'yadm checkout release/'
abbr ycos 'yadm checkout support/'
abbr ycors 'yadm checkout --recurse-submodules'

abbr ycount 'yadm shortlog -sn'

abbr ycp 'yadm cherry-pick'
abbr ycpa 'yadm cherry-pick --abort'
abbr ycpc 'yadm cherry-pick --continue'

abbr yd 'yadm diff'
abbr ydca 'yadm diff --cached'
abbr ydcw 'yadm diff --cached --word-diff'
abbr ydct 'yadm diff --staged'
abbr ydt 'yadm diff-tree --no-commit-id --name-only -r'
# abbr ydnolock 'yadm diff ":(exclude)package-lock.json" ":(exclude)*.lock"'
abbr ydup 'yadm diff @{upstream}'
# abbr ydv 'yadm diff -w $@ | view -'

abbr ydct 'yadm describe --tags (yadm rev-list --tags --max-count=1)'

abbr yf 'yadm fetch'
abbr yfa 'yadm fetch --all --prune'
abbr yfo 'yadm fetch origin'

# gg
# gga
# ggf
# ggfl
# ggl
# ggp
# ggpnp
# ggpull
# ggpur
# ggpush
# ggsup
# ggu
# gpsup

abbr yhh 'yadm help'

abbr yi 'yadm init'

abbr yignore 'yadm update-index --assume-unchanged'
abbr yignored 'yadm ls-files -v | grep "^[[:lower:]]"'

abbr yk 'gitk --all --branches &!'
abbr yke 'gitk --all (yadm log -g --pretty=%h) &!'

abbr yfg 'yadm ls-files | grep'

# gl: yadm log
abbr yl 'yadm log'
abbr yls 'yadm log --stat'
abbr ylsp 'yadm log --stat -p'
abbr ylg 'yadm log --graph'
abbr ylgda 'yadm log --graph --decorate --all'
abbr ylgm 'yadm log --graph --max-count=10'
abbr ylo 'yadm log --oneline --decorate'
abbr ylog 'yadm log --oneline --decorate --graph'
abbr yloga 'yadm log --oneline --decorate --graph --all'
# abbr ylol
# abbr ylols
# abbr ylod
# abbr ylods
# abbr ylola

# gm: yadm merge
abbr ym 'yadm merge'
abbr ymom 'yadm merge origin/main'
abbr ymum 'yadm merge upstream/main'
abbr yma 'yadm merge --abort'

# gmtl: yadm mergetool
abbr ymtl 'yadm mergetool --no-prompt'
abbr ymtlvim 'yadm mergetool --no-prompt --tool=vimdiff'

# gp: yadm push
abbr yp 'yadm push'
abbr ypd 'yadm push --dry-run'
abbr ypf 'yadm push --force-with-lease'
abbr ypf! 'yadm push --force'
abbr ypsu 'yadm push --set-upstream origin (yadm branch --show-current)'
abbr ypt 'yadm push --tags'
abbr yptf 'yadm push --tags --force-with-lease'
abbr yptf! 'yadm push --tags --force'
abbr ypoat 'yadm push origin --all && yadm push origin --tags'
abbr ypoatf! 'yadm push origin --all --force-with-lease && yadm push origin --tags --force-with-lease'
abbr ypoatf! 'yadm push origin --all --force && yadm push origin --tags --force'
abbr ypv 'yadm push -v'

# gpl: yadm pull
abbr ypl 'yadm pull'
abbr yplo 'yadm pull origin'
abbr yplom 'yadm pull origin main'
abbr yplu 'yadm pull upstream'
abbr yplum 'yadm pull upstream main'

# gr: yadm remote
abbr yr 'yadm remote -v'
abbr yra 'yadm remote add'
abbr yrau 'yadm remote add upstream'
abbr yrrm 'yadm remote remove'
abbr yrmv 'yadm remote rename'
abbr yrset 'yadm remote set-url'
abbr yru 'yadm remote update'
abbr yrv 'yadm remote -v'
abbr yrvv 'yadm remote -vvv'

# grb: yadm rebase
abbr yrb 'yadm rebase'
abbr yrba 'yadm rebase --abort'
abbr yrbc 'yadm rebase --continue'
abbr yrbi 'yadm rebase -i'
abbr yrbom 'yadm rebase origin/main'
abbr yrbo 'yadm rebase --onto'
abbr yrbs 'yadm rebase --skip'

# grev: yadm revert
abbr yrev 'yadm revert'

# grs: yadm reset
abbr yrs 'yadm reset'
abbr yrs! 'yadm reset --hard'
abbr yrsh 'yadm reset HEAD'
abbr yrsh! 'yadm reset HEAD --hard'
abbr yrsoh 'yadm reset origin/(yadm branch --show-current)'
abbr yrsoh! 'yadm reset origin/(yadm branch --show-current) --hard'
abbr ypristine 'yadm reset --hard && yadm clean -dffx'
abbr yrs- 'yadm reset --'

# grm: yadm rm
abbr yrm 'yadm rm'
abbr yrmc 'yadm rm --cached'

# grst: yadm restore
abbr yrst 'yadm restore'
abbr yrsts 'yadm restore --source'
abbr yrstst 'yadm restore --staged'

# grt: yadm return
abbr yrt 'cd (yadm rev-parse --show-toplevel || echo .)'

# gs: yadm status
abbr ys 'yadm status'
abbr yss 'yadm status -s'
abbr ysb 'yadm status -sb'

# gshow: yadm show
abbr yshow 'yadm show'
abbr yshowps 'yadm show --pretty=short --show-signature'

# gst: yadm stash
abbr yst 'yadm stash'
abbr ysta 'yadm stash apply'
abbr ystc 'yadm stash clear'
abbr ystd 'yadm stash drop'
abbr ystl 'yadm stash list'
abbr ystp 'yadm stash pop'
abbr ystshow 'yadm stash show --text'
abbr ystall 'yadm stash --all'
abbr ysts 'yadm stash save'

# gsu: yadm submodule
abbr ysu 'yadm submodule update'

# gsw: yadm switch
abbr ysw 'yadm switch'
abbr yswc 'yadm switch -c'
abbr yswm 'yadm switch main'

# gt: yadm tag
abbr yt 'yadm tag'
abbr yts 'yadm tag -s'
abbr yta 'yadm tag -a'
abbr ytas 'yadm tag -a -s'
# gtl

# gwch: yadm whatchanged
abbr ywch 'yadm whatchanged -p --abbrev-commit --pretty=medium'

# gwt: yadm worktree
abbr ywt 'yadm worktree'
abbr ywta 'yadm worktree add'
abbr ywtls 'yadm worktree list'
abbr ywtmv 'yadm worktree move'
abbr ywtrm 'yadm worktree remove'

# gam: yadm am
abbr yam 'yadm am'
abbr yamc 'yadm am --continue'
abbr yams 'yadm am --skip'
abbr yama 'yadm am --abort'
abbr yamscp 'yadm am --show-current-patch'
