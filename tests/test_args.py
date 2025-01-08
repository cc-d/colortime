import pytest
from unittest import mock
from sys import path
from os.path import abspath, dirname, join as opjoin

path.append(opjoin(dirname(abspath(__file__)), ".."))


from unittest.mock import patch


@patch("sys.argv", ['lol', '5', '2.3'])
def test_get_args_argv():
    from args import get_args
    args = get_args()
    assert args == (5, 2.3)

