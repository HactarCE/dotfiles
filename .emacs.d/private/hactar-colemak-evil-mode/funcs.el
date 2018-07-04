;;; funcs.el --- Hactar-Colemak Layer keybindings file for Spacemacs
;; Copyright (c) 2018 HactarCE
;;
;; Author: HactarCE
;; URL: https://github.com/HactarCE/hactar-colemak-evil-mode
;;
;; This file is not part of GNU Emacs.
;;
;;; License: The Unlicense

;; basically straight-up copied from here:
;; https://github.com/wbolster/evil-colemak-basics/blob/master/evil-colemak-basics.el

;; TODO move this to user-config or whatever
(setq-default dotspacemacs-line-numbers 'relative)

(with-eval-after-load 'evil

  ;; prefixes
  ;; TODO doesn't work
  ;; TODO add "a" and "r"?
  (spacemacs/set-leader-keys-for-minor-mode 'hactar-colemak-evil-mode
    (kbd "t") 'insert/visual-mode-prefix
    (kbd "o") 'misc-prefix)

  ;; activate/reset normal mode
  (evil-define-minor-mode-key '(insert motion visual operator replace emacs) 'hactar-colemak-evil-mode
    (kbd "C-o") #'evil-normal-state)
  (evil-define-minor-mode-key 'normal 'hactar-colemak-evil-mode
    (kbd "C-o") #'evil-force-normal-state)

  ;; all except insert mode
  (evil-define-minor-mode-key '(normal motion visual operator) 'hactar-colemak-evil-mode

    ;; basic movement (luynei)
    (kbd "u") #'evil-previous-line
    (kbd "e") #'evil-next-line
    (kbd "n") #'evil-backward-char
    (kbd "i") #'evil-forward-char
    (kbd "l") #'evil-backward-word-begin
    (kbd "y") #'evil-forward-word-end
    (kbd "U") (kbd "5 u")
    (kbd "E") (kbd "5 e")
    ;; (kbd "U") #'evil-scroll-up
    ;; (kbd "E") #'evil-scroll-down
    (kbd "I") (kbd "10 i")
    (kbd "N") (kbd "10 n")
    (kbd "L") #'evil-backward-WORD-begin
    (kbd "Y") #'evil-forward-WORD-end
;;    (kbd "t u") (lambda ()
;;                  "Insert on a new line above."
;;                  (interactive)
;;                  (spacemacs/evil-insert-line-above)
;;                  (evil-previous-line)
;;                  (evil-insert))

    ;; special
    (kbd "`") #'evil-repeat
    (kbd "O") #'evil-ex

    ;; scrolling
    ;; (kbd "j") (lambda (&optional count)
    ;;             "Scroll up COUNT lines and follow with cursor."
    ;;             (interactive "p")
    ;;             (evil-scroll-line-up (or count 1))
    ;;             (evil-previous-line count))
    ;; (kbd "h") (lambda (&optional count)
    ;;             "Scroll down COUNT lines and follow with cursor."
    ;;             (interactive "p")
    ;;             (evil-scroll-line-down (or count 1))
    ;;             (evil-next-line count))
    ;; (kbd "J") (kbd "5 j")
    ;; (kbd "H") (kbd "5 h")
    (kbd "j") (kbd "10 J")
    (kbd "h") (kbd "10 H")
    (kbd "J") #'evil-scroll-line-up
    (kbd "H") #'evil-scroll-line-down

    ;; prefixed movement
    (kbd "o n") #'evil-beginning-of-line
    (kbd "o i") #'evil-end-of-line

    ;; prefixed scrolling (recenter, essentially)
    (kbd "o j") (lambda (&optional count)
                  ;; TODO support count, but default to 5?
                  "Scroll line to near top."
                  (interactive)
                  (recenter-top-bottom 5))
    (kbd "o h") #'evil-scroll-line-to-center
    (kbd "o k") (lambda (&optional count)
                  ;; TODO support count, but default to 5?
                  "Scroll line to near bottom."
                  (interactive)
                  (recenter-top-bottom -5))

    )

  ;; normal mode
  (evil-define-minor-mode-key 'normal 'hactar-colemak-evil-mode

    ;; selection
    (kbd "a") evil-outer-text-objects-map
    (kbd "r") evil-inner-text-objects-map

    ;; basic operators
    (kbd "s") #'evil-change
    (kbd "S") #'evil-change-line
    (kbd "z") #'undo-tree-undo
    (kbd "Z") #'undo-tree-redo
    (kbd "x") #'evil-delete
    (kbd "X") #'evil-delete-line
    (kbd "c") #'evil-yank
    (kbd "C") #'evil-yank-line
    (kbd "v") #'evil-paste-after
    (kbd "V") #'evil-paste-before
    (kbd "p") #'evil-replace
    (kbd "P") #'evil-replace-state

    ;; misc prefix
    (kbd "o u") #'spacemacs/evil-insert-line-above ;; TODO with/without indent
    (kbd "o e") #'spacemacs/evil-insert-line-below
    (kbd "o z") #'undo-tree-visualize

    ;; insert prefix
    (kbd "t u") #'evil-open-above
    (kbd "t e") #'evil-open-below ;; TODO add "t U" and "t E" to open above/below with/without indent
    (kbd "t n") #'evil-insert
    (kbd "t i") #'evil-append
    (kbd "t o n") #'evil-insert-line
    (kbd "t o i") #'evil-append-line
    ;; these don't quite fit, but they're convenient and unassigned
    (kbd "t N") #'evil-insert-line
    (kbd "t I") #'evil-append-line
    ;; TODO add "t l", "t y", "t L", and "t Y"

    ;; visual prefix
    (kbd "t s") #'evil-visual-char
    (kbd "t r") #'evil-visual-line
    (kbd "t a") #'evil-visual-block

    ))

(define-minor-mode hactar-colemak-evil-mode
  "An alternative keymap for Vim commands on Colemak based on ZXCV and UNEI."
  ;; :lighter "unei"
  :lighter "Ⓗ"
  :global t)

(provide 'hactar-colemak-evil-mode)
