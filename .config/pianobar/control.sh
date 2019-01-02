#!/usr/bin/sh

STATUS_FILE="$HOME/.config/pianobar/status"
PIANOBAR_FIFO_FILE="$HOME/.config/pianobar/ctl"
EVENTCMD_FIFO_FILE="$HOME/.config/pianobar/eventcmd_fifo"

if [ -f "$STATUS_FILE" ] && pgrep -x pianobar; then
    case "$1" in
        toggle)
            cat > "$EVENTCMD_FIFO_FILE" <<EOF
toggle
~~~
EOF
            ;;
        play)
            echo -n P > "$PIANOBAR_FIFO_FILE"
            ;;
        pause)
            echo -n S > "$PIANOBAR_FIFO_FILE"
            ;;
        playpause|toggleplaypause)
            echo -n ' ' > "$PIANOBAR_FIFO_FILE"
            ;;
        skip)
            echo -n n > "$PIANOBAR_FIFO_FILE"
            ;;
        quit)
            echo -n q > "$PIANOBAR_FIFO_FILE"
            ;;
        love)
            echo -n + > "$PIANOBAR_FIFO_FILE"
            ;;
        ban)
            echo -n - > "$PIANOBAR_FIFO_FILE"
            ;;
        shelf)
            echo -n t > "$PIANOBAR_FIFO_FILE"
            ;;
        *)
            echo "Allowed commands: toggle, play, pause, playpause, toggleplaypause, skip, quit, love, ban, shelf"
    esac
elif [[ "$1" -eq toggle ]] || [[ "$1" -eq toggleplaypause ]]; then
    i3-sensible-terminal -e "python3 $HOME/.config/pianobar/polianobar.py" -r pianobar -t Pianobar &
else
    echo "Pianobar is not running."
fi
