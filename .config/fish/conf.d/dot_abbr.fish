#!/usr/bin/env fish
#
# dot-abbr: dotfile git abbreviations for the fish shell
#
# Based on git-abbr (Copyright (c) 2022 Rich Lewis, MIT License)

set -g __dot_abbr_version 0.2.1

abbr d 'dot'

abbr da 'dot add'
abbr daa 'dot add --all'
abbr dapa 'dot add --patch'
abbr dau 'dot add --update'
abbr dav 'dot add --verbose'
abbr dap 'dot apply'
abbr dapt 'dot apply --3way'

abbr db 'dot branch'
abbr dba 'dot branch -a'
abbr dbd 'dot branch -d'
abbr dbdf 'dot branch -d -f'
abbr dbD 'dot branch -D'
abbr dbDf 'dot branch -D -f'
abbr dbnm 'dot branch --no-merged'
abbr dbr 'dot branch --remote'

abbr dbl 'dot blame -b -w'

abbr dbs 'dot bisect'
abbr dbsb 'dot bisect bad'
abbr dbsg 'dot bisect good'
abbr dbsr 'dot bisect reset'
abbr dbss 'dot bisect start'

# abbr dc 'dot commit -v'
abbr dci 'dot commit --allow-empty -v -m\'chore: initial commit\''
abbr dc! 'dot commit -v --amend'
abbr dcn 'dot commit -v --no-edit'
abbr dcn! 'dot commit -v --amend --no-edit'
abbr dca 'dot commit -a -v'
abbr dca! 'dot commit -a -v --amend'
abbr dcan! 'dot commit -a -v --no-edit --amend'
abbr dcans! 'dot commit -a -v -s --no-edit --amend'
abbr dcam 'dot commit -a -m'
abbr dcas 'dot commit -a -s'
abbr dcasm 'dot commit -a -s -m'
abbr dcsm 'dot commit -s -m'
abbr dcm 'dot commit -m'
abbr dcs 'dot commit -S'

abbr dcf 'dot config --list'

abbr dcl 'dot clone --recurse-submodules'

abbr dclean 'dot clean -id'

abbr dco 'dot checkout'
abbr dcob 'dot checkout -b'
abbr dcom 'dot checkout (dot_main_branch)'
abbr dcod 'dot checkout (dot_develop_branch)'
abbr dcof 'dot checkout (dot_feature_prepend)/'
abbr dcoh 'dot checkout hotfix/'
abbr dcor 'dot checkout release/'
abbr dcos 'dot checkout support/'
abbr dcors 'dot checkout --recurse-submodules'

abbr dcount 'dot shortlog -sn'

abbr dcp 'dot cherry-pick'
abbr dcpa 'dot cherry-pick --abort'
abbr dcpc 'dot cherry-pick --continue'

abbr ddca 'dot diff --cached'
abbr ddcw 'dot diff --cached --word-diff'
abbr ddct 'dot diff --staged'
abbr ddt 'dot diff-tree --no-commit-id --name-only -r'
# abbr ddnolock 'dot diff ":(exclude)package-lock.json" ":(exclude)*.lock"'
abbr ddup 'dot diff @{upstream}'
# abbr ddv 'dot diff -w $@ | view -'

abbr dl 'dot log'
abbr dls 'dot log --stat'
abbr dlsp 'dot log --stat -p'
abbr dlg 'dot log --graph'
abbr dlgda 'dot log --graph --decorate --all'
abbr dlgm 'dot log --graph --max-count=10'
abbr dlo 'dot log --oneline --decorate'
abbr dlog 'dot log --oneline --decorate --graph'
abbr dloga 'dot log --oneline --decorate --graph --all'
# abbr dlol
# abbr dlols
# abbr dlod
# abbr dlods
# abbr dlola

# dm: dot merge
abbr dm 'dot merge'
abbr dmom 'dot merge origin/(dot_main_branch)'
abbr dmum 'dot merge upstream/(dot_main_branch)'
abbr dma 'dot merge --abort'

# dmtl: dot mergetool
abbr dmtl 'dot mergetool --no-prompt'
abbr dmtlvim 'dot mergetool --no-prompt --tool=vimdiff'

# dp: dot push
abbr dp 'dot push'
abbr dpd 'dot push --dry-run'
abbr dpf 'dot push --force-with-lease'
abbr dpf! 'dot push --force'
abbr dpsu 'dot push --set-upstream origin (dot_current_branch)'
abbr dpt 'dot push --tags'
abbr dptf 'dot push --tags --force-with-lease'
abbr dptf! 'dot push --tags --force'
abbr dpoat 'dot push origin --all && dot push origin --tags'
abbr dpoatf! 'dot push origin --all --force-with-lease && dot push origin --tags --force-with-lease'
abbr dpoatf! 'dot push origin --all --force && dot push origin --tags --force'
abbr dpv 'dot push -v'

# dpl: dot pull
abbr dpl 'dot pull'
abbr dplo 'dot pull origin'
abbr dplom 'dot pull origin (dot_main_branch)'
abbr dplu 'dot pull upstream'
abbr dplum 'dot pull upstream (dot_main_branch)'

# dr: dot remote
abbr dr 'dot remote -v'
abbr dra 'dot remote add'
abbr drau 'dot remote add upstream'
abbr drrm 'dot remote remove'
abbr drmv 'dot remote rename'
abbr drset 'dot remote set-url'
abbr dru 'dot remote update'
abbr drv 'dot remote -v'
abbr drvv 'dot remote -vvv'

# drb: dot rebase
abbr drb 'dot rebase'
abbr drba 'dot rebase --abort'
abbr drbc 'dot rebase --continue'
abbr drbd 'dot rebase (dot_develop_branch)'
abbr drbi 'dot rebase -i'
abbr drbom 'dot rebase origin/(dot_main_branch)'
abbr drbo 'dot rebase --onto'
abbr drbs 'dot rebase --skip'

# drev: dot revert
abbr drev 'dot revert'

# drs: dot reset
abbr drs 'dot reset'
abbr drs! 'dot reset --hard'
abbr drsh 'dot reset HEAD'
abbr drsh! 'dot reset HEAD --hard'
abbr drsoh 'dot reset origin/(dot_current_branch)'
abbr drsoh! 'dot reset origin/(dot_current_branch) --hard'
abbr dpristine 'dot reset --hard && dot clean -dffx'
abbr drs- 'dot reset --'

# drm: dot rm
abbr drm 'dot rm'
abbr drmc 'dot rm --cached'

# drst: dot restore
abbr drst 'dot restore'
abbr drsts 'dot restore --source'
abbr drstst 'dot restore --staged'

# drt: dot return
abbr drt 'cd (dot rev-parse --show-toplevel || echo .)'

# ds: dot status
abbr ds 'dot status'
abbr dss 'dot status -s'
abbr dsb 'dot status -sb'

# dshow: dot show
abbr dshow 'dot show'
abbr dshowps 'dot show --pretty=short --show-signature'

# dst: dot stash
abbr dst 'dot stash'
abbr dsta 'dot stash apply'
abbr dstc 'dot stash clear'
abbr dstd 'dot stash drop'
abbr dstl 'dot stash list'
abbr dstp 'dot stash pop'
abbr dstshow 'dot stash show --text'
abbr dstall 'dot stash --all'
abbr dsts 'dot stash save'

# dsw: dot switch
abbr dsw 'dot switch'
abbr dswc 'dot switch -c'
abbr dswm 'dot switch (dot_main_branch)'
abbr dswd 'dot switch (dot_develop_branch)'

# dt: dot tag
abbr dt 'dot tag'
abbr dts 'dot tag -s'
abbr dta 'dot tag -a'
abbr dtas 'dot tag -a -s'
# dtl

# dwch: dot whatchanged
abbr dwch 'dot whatchanged -p --abbrev-commit --pretty=medium'

# dwt: dot worktree
abbr dwt 'dot worktree'
abbr dwta 'dot worktree add'
abbr dwtls 'dot worktree list'
abbr dwtmv 'dot worktree move'
abbr dwtrm 'dot worktree remove'

# dam: dot am
abbr dam 'dot am'
abbr damc 'dot am --continue'
abbr dams 'dot am --skip'
abbr dama 'dot am --abort'
abbr damscp 'dot am --show-current-patch'
