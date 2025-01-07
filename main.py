#!/usr/bin/env python3
from datetime import datetime as dt, UTC
from time import sleep
from args import DELAY, REPEAT

# Foreground and Background colors
FG_COLORS = [
    ("\033[31m", "red"),
    ("\033[93m", "bright yellow"),
    ("\033[92m", "bright green"),
]

BG_COLORS = [
    ("\033[40m", "black"),
    ("\033[42m", "green"),
    ("\033[43m", "yellow"),
    ("\033[44m", "blue"),
    ("\033[45m", "magenta"),
    ("\033[46m", "cyan"),
    ("\033[47m", "white"),
]

# Precompute all foreground-background color combinations
VAL_COLORS = [
    f"{fg[0]}{bg[0]}" for bg in BG_COLORS for fg in FG_COLORS if fg[1] != bg[1]
]
NUM_COLORS = len(VAL_COLORS)


def write_time(color_idx: int) -> None:
    """Write the current time with color formatting."""
    now = dt.now(UTC).strftime("%H:%M:%S")
    color = VAL_COLORS[color_idx]
    formatted_time = f"{color}{now[1:]}\033[0m"
    print(formatted_time)


def main() -> None:
    color_idx = 0
    repeat_count = 0

    while True:
        write_time(color_idx)
        sleep(DELAY)

        # Update repeat count and color index
        repeat_count += 1
        if repeat_count >= REPEAT:
            repeat_count = 0
            color_idx = (color_idx + 1) % NUM_COLORS


if __name__ == "__main__":
    main()

