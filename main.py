#!/usr/bin/env python3
from argparse import ArgumentParser
from datetime import datetime as dt, UTC
from time import sleep
from sys import stdout
from typing import Callable, List
from args import DELAY, REPEAT

# Foreground color codes
#FG_COLORS = [
#    # ("\033[30m", "black", ["bright black"]),
#    ("\033[31m", "red", ["red", "bright black"]),
#    ("\033[32m", "green", ["blue", "bright black"]),
#    # ("\033[33m", "yellow", ["bright black"]),
#    #("\033[34m", "blue", ["bright black"]),
#    ("\033[35m", "magenta", ["bright black"]),
#    ("\033[36m", "cyan", ["bright black"]),
#    # ("\033[37m", "white", ["bright black"]),
#    # ("\033[91m", "bright red", ["red", "bright black"]),
#    # ("\033[92m", "bright green", ["bright black"]),
#    ("\033[93m", "bright yellow", ["bright black"]),
#    # ("\033[94m", "bright blue", ["bright black"]),
#    # ("\033[95m", "bright magenta", ["bright black"]),
#    # ("\033[96m", "bright cyan", ["bright black"]),
#    # ("\033[97m", "bright white", ["bright black"]),
#]
#
#
## Background color codes
#BG_COLORS = [
#    ("\033[40m", "black", {"bright black"}),
#    ("\033[41m", "red", {"bright red"}),
#    ("\033[42m", "green", {"bright green", "blue", "bright blue"}),
#    ("\033[43m", "yellow", {"bright yellow"}),
#    (
#        "\033[44m",
#        "blue",
#        {"bright blue", "magenta", "bright magenta", "yellow"},
#    ),
#    ("\033[45m", "magenta", {"bright magenta"}),
#    ("\033[46m", "cyan", {"bright cyan"}),
#    ("\033[47m", "white", {"bright white", "bright black"}),
#    ("\033[100m", "bright black", {"black", "magenta"}),
#    ("\033[101m", "bright red", { "magenta", "black"}),
#    ("\033[102m", "bright green", {"green", "cyan", "yellow"}),
#    ("\033[103m", "bright yellow", {"yellow", "white", "bright white"}),
#    (
#        "\033[104m",
#        "bright blue",
#        {"blue", "cyan", "bright white", "bright green", "green"},
#    ),
#    ("\033[105m", "bright magenta", {"magenta", "bright white"}),
#    ("\033[106m", "bright cyan", {"cyan", "bright white", "yellow", "green"}),
#    # ("\033[107m", "bright white", {'white', 'bright white', 'yellow', 'bright yellow'}),
#]

FG_COLORS = [
    # ("\033[30m", "black"),
    ("\033[31m", "red"),
    ("\033[93m", "bright yellow"),

    # ("\033[32m", "green"),
    #("\033[94m", "bright blue"),
    # ("\033[33m", "yellow"),
    # ("\033[34m", "blue"),
    #("\033[35m", "magenta"),
    #("\033[36m", "cyan"),
    # ("\033[37m", "white"),
    # ("\033[91m", "bright red"),
    ("\033[92m", "bright green"),
    
    # ("\033[94m", "bright blue"),
    # ("\033[95m", "bright magenta"),
    # ("\033[96m", "bright cyan"),
    # ("\033[97m", "bright white"),
]

BG_COLORS = [
    ("\033[40m", "black"),
    # ("\033[41m", "red"),
    ("\033[42m", "green"),
    ("\033[43m", "yellow"),
    ("\033[44m", "blue"),
    ("\033[45m", "magenta"),
    ("\033[46m", "cyan"),
    ("\033[47m", "white"),
    ("\033[100m", "bright black"),
    # ("\033[101m", "bright red"),
    # ("\033[102m", "bright green"),
    # ("\033[103m", "bright yellow"),
    # ("\033[104m", "bright blue"),
    # ("\033[105m", "bright magenta"),
    ("\033[106m", "bright cyan"),
    # ("\033[107m", "bright white"),
]

VAL_COLORS: List[str] = [
    fg[0] + bg[0]
    for bg in BG_COLORS
    for i in range(REPEAT)
    for fg in FG_COLORS
    if fg[1] != bg[1] and bg[1] 
]


def get_color(seconds: int) -> str:
    idx, ccount = 0, len(VAL_COLORS)
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


def write_time(wf: Callable[[str], None], msg: str) -> str:
    hr, mn, sec = map(int, msg.split(":"))
    total_seconds = (60 * 60 * hr) + (60 * mn) + sec
    color = get_color(total_seconds)
    formatted_time = (
        f"{color}{hr if hr < 10 else str(hr)[1:]}:{mn:02}:{sec:02}\033[0m\n"
    )
    wf(formatted_time)
    return formatted_time


def main() -> None:
    wf: Callable[[str], None] = stdout.write
    last_time: str | None = None
    while True:
        current_time = dt.now(UTC).strftime("%H:%M:%S")
        if current_time != last_time:
            write_time(wf, current_time)
            last_time = current_time
        sleep(DELAY)


if __name__ == "__main__":
    main()
