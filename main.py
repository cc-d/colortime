#!/usr/bin/env python3
from datetime import datetime as dt, timezone as tz, timedelta

from time import sleep
import typing as _T
from args import get_args
from random import shuffle
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


def get_time() -> str:
    return dt.now(dt.time(tz.utc)).strftime("%H:%M:%S")[1:]


class ColorCell:
    def __init__(self, fg: str, bg: str):
        self.fg, self.bg = fg, bg

    def __str__(self) -> str:
        return f'{self.fg[0]}{self.bg[0]}{get_time()}\033[0m'


class ColorPool:
    pool: _T.List[ColorCell] = []
    fg_colors: _T.List = FG_COLORS
    bg_colors: _T.List[_T.Tuple] = list(shuffle(BG_COLORS))

    def __init__(
        self, repeat: int, delay: int, num_cols: int, col_offset: int
    ):
        self.repeat, self.delay = repeat, delay
        self.num_cols, self.col_offset = num_cols, col_offset

    def populate(self) -> _T.List[ColorCell]:
        last_start = None if self.pool == [] else self.pool[0]
        self.pool = [
            ColorCell(fg[0], bg[0])
            for bg in self.bg_colors
            for fg in self.fg_colors
            if fg[1] != bg[1]
        ]
        while self.pool[0].fg == last_start.fg:
            self.pool.append(self.pool.pop(0))

    def run(self):
        self.populate()
        _plen, _curidx, _pbuff = len(self.pool), 0, ''

        while True:
            for i in range(_plen):
                _pbuff += self.pool[i]


def main(): ...


'''
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

'''

if __name__ == "__main__":
    main()  # pragma: no cover
