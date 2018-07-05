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
;; TODO doesn't work for not-yet-opened buffers
(setq-default dotspacemacs-line-numbers 'relative)
;; (setq avy-keys '(?a ?r ?s ?t ?d ?h ?n ?e ?i ?o))
;; (setq avy-keys '(?a ?r ?s ?t ?d ?h ?n ?e ?i ?o ?q ?w ?f ?p ?l ?u ?y))
(setq avy-keys '(?a ?r ?s ?t ?n ?e ?i ?o ?w ?f ?p ?l ?u ?y))

(with-eval-after-load 'evil

  ;; prefixes
  ;; TODO doesn't work
  ;; TODO add "a" and "r"?
  (spacemacs/set-leader-keys-for-minor-mode 'hactar-colemak-evil-mode
    (kbd "t") 'insert/visual-mode-prefix
    (kbd "o") 'misc-prefix)

  ;; all except emacs mode
  (evil-define-minor-mode-key '(insert motion visual operator replace normal) 'hactar-colemak-evil-mode
    (kbd "C-/") #'comment-line
    )

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
    ;; (kbd "l") #'evil-backward-word-begin
    ;; (kbd "y") #'evil-forward-word-end
    (kbd "U") (kbd "5 u")
    (kbd "E") (kbd "5 e")
    ;; (kbd "U") #'evil-scroll-up
    ;; (kbd "E") #'evil-scroll-down
    (kbd "I") (kbd "10 i")
    (kbd "N") (kbd "10 n")
    ;; (kbd "L") #'evil-backward-WORD-begin
    ;; (kbd "Y") #'evil-forward-WORD-end
    ;; (kbd "t u") (lambda ()
    ;;               "Insert on a new line above."
    ;;               (interactive)
    ;;               (spacemacs/evil-insert-line-above)
    ;;               (evil-previous-line)
    ;;               (evil-insert))

    ;; special
    (kbd "`") #'evil-repeat
    (kbd "O") #'evil-ex
    ;; (kbd "o o") #'helm-M-x

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
    ;; (kbd "j") (kbd "10 J")
    ;; (kbd "h") (kbd "10 H")
    ;; (kbd "J") #'evil-scroll-line-up
    ;; (kbd "H") #'evil-scroll-line-down
    (kbd "l") (kbd "10 L")
    (kbd "m") (kbd "10 M")
    (kbd "L") #'evil-scroll-line-up
    (kbd "M") #'evil-scroll-line-down

    ;; avy motion ("Find")
    (kbd "f l") #'evil-avy-goto-line ; "Find Line"
    (kbd "f u") #'evil-avy-goto-line-above
    (kbd "f e") #'evil-avy-goto-line-below
    (kbd "f r") #'evil-avy-goto-char ; "Find chaR"
    (kbd "f s") #'evil-avy-goto-char-timer ; "Find charS"
    (kbd "f w") #'evil-avy-goto-word-or-subword-1 "Find Word"

    ;; "d" prefix
    (kbd "d l") (kbd "x x V V u")

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
    ;; (kbd "a") evil-outer-text-objects-map
    ;; (kbd "r") evil-inner-text-objects-map

    ;; basic operators
    (kbd "s") #'evil-change ; "Substitute"
    (kbd "S") #'evil-change-line
    (kbd "z") #'undo-tree-undo
    (kbd "Z") #'undo-tree-redo
    (kbd "x") #'evil-delete
    (kbd "X") #'evil-delete-line
    (kbd "c") #'evil-yank ; "Copy"
    (kbd "C") #'evil-yank-line
    (kbd "v") #'evil-paste-after ; "Paste"
    (kbd "V") #'evil-paste-before
    (kbd "p") #'evil-replace ; "rePlace"
    (kbd "P") #'evil-replace-state

    ;; misc prefix
    (kbd "o u") #'spacemacs/evil-insert-line-above ;; TODO with/without indent
    (kbd "o e") #'spacemacs/evil-insert-line-below
    (kbd "o z") #'undo-tree-visualize

    ;; insert prefix ("inserT")
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
