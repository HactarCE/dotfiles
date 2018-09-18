#!/usr/bin/sh

STATUS_FILE="$HOME/.config/pianobar/status"
PIANOBAR_FIFO_FILE="$HOME/.config/pianobar/ctl"
EVENTCMD_FIFO_FILE="$HOME/.config/pianobar/eventcmd_fifo"

start_polianobar () {
    i3-sensible-terminal -e "python3 $HOME/.config/pianobar/polianobar.py" -r pianobar -t Pianobar
}

if [ -f "$STATUS_FILE" ] && pkill -0 pianobar; then
    case "$1" in
        toggle)
            cat > "$EVENTCMD_FIFO_FILE" <<EOF
toggle
~~~
EOF
            ;;
        play)
            echo P > "$PIANOBAR_FIFO_FILE"
            ;;
        pause)
            echo S > "$PIANOBAR_FIFO_FILE"
            ;;
        playpause|toggleplaypause)
            echo ' ' > "$PIANOBAR_FIFO_FILE"
            ;;
        skip)
            echo n > "$PIANOBAR_FIFO_FILE"
            ;;
        quit)
            echo q > "$PIANOBAR_FIFO_FILE"
            ;;
        love)
            echo + > "$PIANOBAR_FIFO_FILE"
            ;;
        ban)
            echo - > "$PIANOBAR_FIFO_FILE"
            ;;
        shelf)
            echo t > "$PIANOBAR_FIFO_FILE"
            ;;
        *)
            echo "Allowed commands: toggle, play, pause, playpause, toggleplaypause, skip, quit, love, ban, shelf"
    esac
elif [[ "$1" -eq toggle ]] || [[ "$1" -eq toggleplaypause ]]; then
    start_polianobar
else
    echo "Pianobar is not running."
fi
