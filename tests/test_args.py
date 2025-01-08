import pytest
from sys import path
from os.path import abspath, dirname, join as opjoin

path.append(opjoin(dirname(abspath(__file__)), ".."))
from args import get_args, DELAY, REPEAT, argv

from unittest.mock import patch


@patch("sys.argv", ["lol", "5", "2.3"])
def test_get_args_argv():
    assert get_args() == (5, 2.3)
    print(get_args())
