from argparse import ArgumentParser
from sys import argv
from typing import Tuple as T

# Default values
REPEAT, DELAY = 8, 1.89


def get_args() -> T[int, float]:

    parser = ArgumentParser()
    parser.add_argument(
        "repeat",
        type=int,
        nargs="?",
        default=REPEAT,
        help="Number of repeats for color sequence",
    )
    parser.add_argument(
        "delay",
        type=float,
        nargs="?",
        default=DELAY,
        help="Delay between updates in seconds",
    )
    args = parser.parse_args()
    return (args.repeat, args.delay)
