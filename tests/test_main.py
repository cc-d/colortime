import pytest
from sys import path
from os.path import abspath, dirname, join as opjoin

path.append(opjoin(dirname(abspath(__file__)), ".."))

from unittest.mock import patch
from main import (
    write_time,
    get_color,
    get_time,
    VAL_COLORS,
    main,
    repeat,
    NUM_COLORS,
    REPEAT,
)


def test_get_time():
    t = get_time()
    assert len(t.split(":")[0]) == 1


def test_get_color():
    for i in range(len(VAL_COLORS)):
        assert get_color(i) == VAL_COLORS[i]


def test_write_time():
    color = get_color(0)
    wt = write_time(color)
    assert wt.endswith("\033[0m")
    assert wt.startswith(color[0:4])


def test_repeat():
    count, idx = REPEAT - 1, 20
    assert repeat(count, idx) == (0, 0 % NUM_COLORS)

    count, idx = REPEAT - 1, 3
    assert repeat(count, idx) == (0, (3 + 1) % NUM_COLORS)


@patch("main.sleep", side_effect=KeyboardInterrupt)
def test_main(msleep):
    main()


from args import get_args, DELAY, REPEAT, argv


@patch("args.argv", ["lol", 5, 2.3])
def test_get_args_argv():
    assert get_args() == (5, 2.3)
    print(get_args())
