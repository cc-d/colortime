from main import write_time, get_color, VAL_COLORS
from unittest import TestCase, main


class TestMain(TestCase):

    def test_print(self):
        for hr in range(4):
            for mn in range(0,60):
                for sec in range(0, 60):
                    time_str = f"{hr:02}:{mn:02}:{sec:02}"
                    write_time(print, time_str)


if __name__ == "__main__":
    main()
