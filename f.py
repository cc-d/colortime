#!/usr/bin/env python3
from datetime import datetime as dt
from time import sleep
from sys import argv, stdout
from os import system
from typing import Callable

FG_COLORS = [
    ("\033[97m", "white"),
    ("\033[93m", "yellow"),
    ("\033[92m", "green"),
    ("\033[96m", "cyan"),
    ("\033[94m", "blue"),
    ("\033[91m", "red"),
    ("\033[95m", "magenta"),
]

BG_COLORS = [
    ("\033[40m", "black"),
    ("\033[41m", "red"),
    ("\033[44m", "blue"),
    ("\033[45m", "magenta"),
    ("\033[42m", "green"),
    ("\033[100m", "gray"),
]

if any("tests" in a for a in argv):
    argv = [a for a in argv if "tests" not in a]


REPEAT = 5 if len(argv) < 3 else int(argv[2])
DELAY = 1.0 if len(argv) < 2 else float(argv[1])


VAL_COLORS = []


VAL_COLORS = [
    fg[0] + bg[0]
    for bg in BG_COLORS
    for i in range(REPEAT)
    for fg in FG_COLORS
    if fg[1] != bg[1]
]


def get_color(seconds: int | float) -> str:
    idx = 0
    ccount = len(VAL_COLORS)
    while seconds > 0:

        if seconds - ccount * REPEAT > 0:
            seconds -= ccount * REPEAT
            idx = 0
        else:
            seconds -= REPEAT
            idx += 1
            if idx >= len(VAL_COLORS):
                idx = 0
    return VAL_COLORS[idx]


def write_time(wf: Callable, msg: str) -> str:
    hr, mn, sec = map(int, msg.split(":"))
    total_seconds = (60 * 60 * hr) + (60 * mn) + sec
    color = get_color(total_seconds)
    wf(f"{color}" + f"{str(hr)[1:]}:{mn:02}:{sec:02}\033[0m\033\n")
    return f"{color}"


def main() -> None:
    wf = stdout.write
    last_time = None
    while True:
        current_time = dt.now().isoformat().split("T")[1].split(".")[0]
        if last_time is not None and last_time != current_time:
            write_time(wf, current_time)

        sleep(DELAY)


if __name__ == "__main__":

    main()
