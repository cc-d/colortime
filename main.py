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
    return dt.utcnow().strftime("%H:%M:%S")


def colorstr(fg: str, bg: str, s: str) -> str:
    return f'{fg}{bg}{s}\033[0m'


class ColorPool:
    pool: _T.List = []
    fg_colors: _T.List = FG_COLORS
    bg_colors: _T.List[_T.Tuple] = list(BG_COLORS)
    last_color = None

    def __init__(
        self, repeat: int, delay: int, num_cols: int, col_offset: int
    ):
        self.repeat, self.delay = repeat, delay
        self.num_cols, self.col_offset = num_cols, col_offset

    def populate(self):
        shuffle(self.bg_colors)
        shuffle(self.fg_colors)
        self.pool = [
            (fg, bg)
            for bg in self.bg_colors
            for fg in self.fg_colors
            if fg[1] != bg[1]
        ]
        if self.last_color is None:
            return
        while self.pool[0][0] == self.last_color[0]:
            self.pool.append(self.pool.pop(0))

    def run(self):
        self.populate()
        pool_len = len(self.pool)

        # Initialize columns with different starting positions based on col_offset
        columns = []
        base_idx = 0

        for c in range(self.num_cols):
            # Calculate offset index for this column
            offset_idx = (base_idx + (c * self.col_offset)) % pool_len
            columns.append({"idx": offset_idx, "count": 0})

        # Track color exhaustion
        total_colors_used = 0
        need_reshuffle = False

        while True:
            line = ''
            all_complete_cycle = True

            for col in range(self.num_cols):
                cur_col = columns[col]
                color_pair = self.pool[cur_col["idx"]]

                # Add colored time to the line
                line += colorstr(
                    color_pair[0][0], color_pair[1][0], get_time()
                )

                # Increment the counter
                cur_col["count"] += 1

                # If counter reaches repeat value, change the color
                if cur_col["count"] >= self.repeat:
                    cur_col["count"] = 0
                    cur_col["idx"] = (cur_col["idx"] + 1) % pool_len
                    # Remember the last color used
                    self.last_color = self.pool[cur_col["idx"]]

                    # Check if we've used all colors
                    total_colors_used += 1
                    if total_colors_used >= pool_len:
                        need_reshuffle = True
                else:
                    # If any column hasn't completed its cycle, we don't reshuffle yet
                    all_complete_cycle = False

            # Print the full line and sleep
            print(line)
            sleep(self.delay)

            # Only reshuffle if we need to AND all columns have completed their current cycles
            if need_reshuffle and all_complete_cycle:
                self.populate()
                pool_len = len(self.pool)
                total_colors_used = 0
                need_reshuffle = False

                # Update column indices to stay in valid range
                for col in columns:
                    col["idx"] = col["idx"] % pool_len


def main():
    ct = ColorPool(*get_args())
    ct.populate()
    ct.run()


if __name__ == "__main__":
    main()  # pragma: no cover
