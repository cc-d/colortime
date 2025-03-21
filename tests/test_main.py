import pytest as pt
from sys import path
from os.path import abspath, dirname, join as opjoin

path.append(opjoin(dirname(abspath(__file__)), ".."))

from unittest.mock import patch
from main import get_time, NUM_COLORS, next_color


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
