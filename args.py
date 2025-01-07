from argparse import ArgumentParser
from sys import argv

# Skip argument parsing if running with unittest
if "unittest" in argv or "tests" in argv:
    DELAY = 1.0  # Default delay
    REPEAT = 5  # Default repeat
else:
    parser = ArgumentParser()

    parser.add_argument(
        "repeat",
        type=int,
        nargs="?",
        default=3,
        help="Number of repeats for color sequence",
    )
    parser.add_argument(
        "delay",
        type=float,
        nargs="?",
        default=1.0,
        help="Delay between updates in seconds",
    )

    args = parser.parse_args()
    DELAY = args.delay
    REPEAT = args.repeat
