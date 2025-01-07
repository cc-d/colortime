from argparse import ArgumentParser
from sys import argv

# Skip argument parsing if running with unittest

DELAY = 1.89  # Default delay
REPEAT = 8  # Default repeat

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
DELAY = args.delay
REPEAT = args.repeat
