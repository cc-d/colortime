import pytest as pt
from sys import path
from os.path import abspath, dirname, join as opjoin

path.append(opjoin(dirname(abspath(__file__)), ".."))

from unittest.mock import patch
from main import (
    write_time,
    get_color,
    get_time,
    colors,
    NUM_COLORS,
    next_color,
)


def test_write_time():
    for i in range(len(colors)):
        cur_time = get_time()
        cur_color = get_color(i)
        with patch('main.get_time') as mock_gt:
            mock_gt.return_value = cur_time
            assert write_time(cur_color) == f'{cur_color}{cur_time}\33[0m'


@pt.mark.parametrize(
    'count, color_idx, repeat',
    [
        (0, 0, 5),  # Standard increment
        (4, 0, 5),  # Last iteration before rollover
        (0, len(colors) - 1, 5),  # Rollover to the beginning of VAL_COLORS
        (4, len(colors) - 1, 5),  # Last iteration before full rollover
    ],
)
def test_next_color(count, color_idx, repeat):
    new_count, new_color_idx = next_color(count, color_idx, repeat)

    if count + 1 < repeat:
        assert new_count == count + 1
        assert new_color_idx == color_idx
    else:
        assert new_count == 0
        assert new_color_idx == (color_idx + 1) % NUM_COLORS


from io import StringIO
import sys
from main import main


@pt.mark.parametrize("max_repeats, interval", [(5, 0.1), (1, 1.0), (10, 0.05)])
def test_main_with_args(max_repeats, interval):
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    with patch(
        "sys.argv", ["main.py", str(max_repeats), str(interval)]
    ), patch("main.sleep") as mock_sleep:

        def mock_sleep_effect(_):
            if mock_sleep.call_count >= max_repeats:
                raise KeyboardInterrupt

        mock_sleep.side_effect = mock_sleep_effect

        try:
            main()
        except KeyboardInterrupt:
            pass

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    output_lines = output.strip().splitlines()
    assert len(output_lines) == max_repeats
    assert mock_sleep.call_count == max_repeats
    sleep_args = mock_sleep.call_args_list[0].args
    assert set(sleep_args) == {interval}
