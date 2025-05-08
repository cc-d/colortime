#!/usr/bin/env python3
from datetime import datetime as dt, UTC
from time import sleep

from typing import Tuple as T
from args import get_args

from random import choice, randint

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


def get_colortime(idx: str) -> str:
    color = VAL_COLORS[idx]
    return f"{color}{get_time()}\033[0m"


def next_color(count: int, color_idx: int, repeat: int) -> T[int, int]:
    count += 1
    if count >= repeat:
        count = 0
        color_idx += 1

        if color_idx >= NUM_COLORS:
            color_idx = 0

    return count, color_idx


def main():
    _repeat, _delay, _col_count, _col_offset = get_args()
    cur_count, col_idx = 0, 0

    columns = [[] for _ in range(_col_count)]
    for c in range(_col_count):
        columns[(c + 1) * -1] = [cur_count, col_idx]
        if len(columns) == c - 1:
            break
        for _ in range(_col_offset):
            cur_count, col_idx = next_color(cur_count, col_idx, _repeat)

    while True:
        cline = ''
        for c in columns:
            cline += get_colortime(c[1])

            c[0], c[1] = next_color(c[0], c[1], _repeat)
        print(cline)
        # cur_count, col_idx = next_color(cur_count, col_idx, _repeat)
        sleep(_delay)


if __name__ == "__main__":
    main()  # pragma: no cover
