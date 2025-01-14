from typing import Tuple as T

_DEFAULTS = (6, 0.1, 4, 2)

from argparse import ArgumentParser


def get_args() -> T[int, float, int, int]:
    parser = ArgumentParser()
    parser.add_argument(
        "repeat",
        type=int,
        nargs="?",
        default=_DEFAULTS[0],
        help="Number of repeats for color sequence",
    )
    parser.add_argument(
        "delay",
        type=float,
        nargs="?",
        default=_DEFAULTS[1],
        help="Delay between updates in seconds",
    )
    parser.add_argument(
        'columns',
        type=int,
        nargs='?',
        default=_DEFAULTS[2],
        help="Number of columns of colored times",
    )
    parser.add_argument(
        'column_offset',
        type=int,
        nargs='?',
        help='Background/foreground offset between columns',
        default=_DEFAULTS[3],
    )
    args = parser.parse_args()
    return (args.repeat, args.delay, args.columns, args.column_offset)
