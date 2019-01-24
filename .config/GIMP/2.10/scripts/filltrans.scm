;;; http://gimpchat.com/viewtopic.php?f=9&t=3153

; filltrans.scm
; by Rob Antonishen
; http://ffaat.pointclark.net

; Version 1.1 (20111102)

; History
; V1.1 added size selector and improved speed by working in a new image.

; Description
; Fills the transparent parts of a layer by bleeding out the colour into the transparent regions.

; License:
;
; This program is free software; you can redistribute it and/or modify
; it under the terms of the GNU General Public License as published by
; the Free Software Foundation; either version 2 of the License, or
; (at your option) any later version.
;
; This program is distributed in the hope that it will be useful,
; but WITHOUT ANY WARRANTY; without even the implied warranty of
; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
; GNU General Public License for more details.
;
; The GNU Public License is available at
; http://www.gnu.org/copyleft/gpl.html

(define (filltrans img inLayer inStep inDist inTransfer)
  (let*
    (
      (inStep (/ inStep 2))
      (inDist (* inDist 5))
      (imgO img)
      (inLayerO inLayer)
      (img (car (gimp-image-duplicate img)))
      (inLayer (car (gimp-image-get-active-layer img)))
      (blurLayer (car (gimp-layer-copy inLayer TRUE)))
      (alphaVal 0)
      (blursize inStep)
      (alphasel 0)
      (alphaselO 0)
      (buffer "ftbuff")
      (inc 0)
    )
    ;  it begins here
    (gimp-context-push)
    (gimp-image-undo-group-start imgO)

	(gimp-progress-init "Flooding out Colour" -1)

    (gimp-selection-layer-alpha inLayerO)
    (set! alphaselO (car (gimp-selection-save imgO)))
    (gimp-selection-none imgO)

    (gimp-selection-layer-alpha inLayer)
    (set! alphasel (car (gimp-selection-save img)))
    (gimp-selection-none img)

    (gimp-image-undo-disable img)
    (gimp-image-add-layer img blurLayer (+ (car (gimp-image-get-layer-position img inLayer)) 1))

    (plug-in-threshold-alpha RUN-NONINTERACTIVE img inLayer 254)
    (plug-in-threshold-alpha RUN-NONINTERACTIVE img blurLayer 254)

    (while (< alphaVal 1)
      (gimp-selection-layer-alpha blurLayer)
      (gimp-selection-border img blursize)
      (gimp-selection-sharpen img)
      (if (equal? (car (gimp-selection-is-empty img)) FALSE)
        (plug-in-gauss RUN-NONINTERACTIVE img blurLayer blursize blursize 0)
      )

      (if (= inDist 0)
        (begin
          (gimp-progress-update alphaVal)
          (gimp-progress-set-text (string-append "Flooding out Colour: " (number->string (floor (* alphaVal 100))) "%"))
        )
        (begin
          (gimp-progress-update (/ inc inDist))
          (gimp-progress-set-text (string-append "Flooding out Colour: " (number->string (floor (* (/ inc inDist) 100))) "%"))
        )
      )

      (gimp-levels blurLayer HISTOGRAM-ALPHA 0 128 1 0 255)
      (gimp-selection-none img)
      (set! alphaVal (list-ref (gimp-histogram blurLayer HISTOGRAM-ALPHA 255 255) 5))

      (set! inc (+ inc blursize))
      (if (and (> inDist 0) (> inc inDist))
        (set! alphaVal 1)
      )
      (set! blursize (+ blursize inStep))
    )

    (gimp-selection-layer-alpha inLayer)
    (gimp-selection-invert img)

    (plug-in-gauss RUN-NONINTERACTIVE img blurLayer (* inStep 2) (* inStep 2) 0)

    (gimp-image-remove-layer img inLayer)

    (when (> inDist 0)
      (gimp-selection-load alphasel)
      (gimp-selection-grow img (/ inDist 5))
      (gimp-selection-invert img)
      (gimp-edit-clear blurLayer)
    )

    (gimp-selection-none img)

    (set! buffer (car (gimp-edit-named-copy blurLayer buffer)))
    (gimp-floating-sel-anchor (car (gimp-edit-named-paste inLayerO buffer TRUE)))

    (gimp-image-delete img)

    (when (equal? inTransfer TRUE)
      (gimp-selection-load alphaselO)
      (gimp-layer-add-mask inLayerO (car (gimp-layer-create-mask inLayerO ADD-SELECTION-MASK)))
      (gimp-selection-none imgO)
      (gimp-layer-set-edit-mask inLayerO FALSE)
    )

    (gimp-image-remove-channel imgO alphaselO)

    (gimp-displays-flush)
    (gimp-image-undo-group-end imgO)

    (gimp-context-pop)
  )
)

(script-fu-register "filltrans"
        		    "<Image>/Layer/Transparency/Bleed Colour into Transparent Areas..."
                    "Bleeds out colours until there is no transparency."
                    "Rob Antonishen"
                    "Rob Antonishen"
                    "Aug 2011"
                    "RGB* GRAY*"
                    SF-IMAGE      "image"      0
                    SF-DRAWABLE   "drawable"   0
					SF-ADJUSTMENT "Start and Step Size" (list 1 1 20 1 5 0 SF-SLIDER)
					SF-ADJUSTMENT "Distance (0 for full layer)" (list 0 0 200 1 10 0 SF-SLIDER)
                    SF-TOGGLE     "Transfer alpha to layer mask" TRUE
)
