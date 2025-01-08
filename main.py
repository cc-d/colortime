#!/usr/bin/env python3
from datetime import datetime as dt, UTC
from time import sleep
from args import DELAY, REPEAT
from typing import Tuple as T

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


def get_time() -> str:
    return dt.now(UTC).strftime("%H:%M:%S")[1:]


def get_color(idx: int) -> str:
    return VAL_COLORS[idx]


def write_time(color: str) -> str:
    """Write the current time with color formatting."""
    fmt_time = f"{color}{get_time()}\033[0m"
    print(fmt_time)
    return fmt_time


def repeat(count: int, color_idx: int) -> T[int, int]:
    count += 1
    if count >= REPEAT:
        count = 0
        color_idx = (color_idx + 1) % NUM_COLORS

    return count, color_idx


def main(): # pragma: no cover
    count, idx = 0, 0 # pragma: no cover
    while True:
        write_time(get_color(idx))
        count, idx = repeat(count, idx)
        sleep(DELAY)


if __name__ == "__main__":  # noqa: dumb
    main()  # pragma: no cover
