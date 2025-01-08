import argparse as ap

from typing import Tuple as T
REPEAT, DELAY = 8, 1.89
def get_args() -> T[int, float]:
    parser = ap.ArgumentParser()
    parser.add_argument(
        "repeat",
        type=int,
        nargs="?",
        default=8,
        help="Number of repeats for color sequence",
    )
    parser.add_argument(
        "delay",
        type=float,
        nargs="?",
        default=1.89,
        help="Delay between updates in seconds",
    )
    args = parser.parse_args()
    return (args.repeat, args.delay)

if __name__ == '__main__':
    REPEAT, DELAY = get_args() # pragma: no cover