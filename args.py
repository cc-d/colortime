from typing import Tuple as T

_DEFAULTS = (8, 1.89)

from argparse import ArgumentParser


def get_args() -> T[int, float]:
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
    args = parser.parse_args()
    return (args.repeat, args.delay)
