import os
import sys
import termios
import tty
from contextlib import contextmanager

INTERRUPT = 3
UP_KEY = 65
DOWN_KEY = 66
RIGHT_KEY = 67
LEFT_KEY = 68

NEXT_KEYS = (RIGHT_KEY, DOWN_KEY)
PREV_KEYS = (LEFT_KEY, UP_KEY)


@contextmanager
def raw_stdin():
    """
    This context manager makes sure to put stdin into raw mode before reading
    any data. After the context is done it resets to previous settings.
    """
    try:
        fd = sys.stdin.fileno()
        settings = termios.tcgetattr(fd)
        tty.setraw(fd)
        yield
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, settings)


class Presentation:

    def __init__(self):
        self._slides = []
        self._current_slide = None
        self._next_slide = None
        self._previous_slide = None

    def __call__(self):
        self.next()

    def __repr__(self):
        return (f'<Presentation: current_slide: {self._current_slide}, '
                f'next_slide: {self._next_slide}, '
                f'previous_slide: {self._previous_slide}')

    def __clear(self):
        os.system('clear')

    def add_slide(self, func):
        self._slides.append(func)

    def current(self):
        if self._current_slide:
            self.__clear()
            self._current_slide()

    def next(self):
        self.__clear()

        if not self._current_slide:
            self._next_slide = self._slides[0]

        if not self._next_slide:
            return self._current_slide()

        # Defines current slide
        self._current_slide = self._next_slide
        current_slide_pointer = self._slides.index(self._current_slide)

        # Defines previous slide
        if current_slide_pointer > 0:
            self._previous_slide = self._slides[current_slide_pointer - 1]

        # Defines next slide
        # If it's last slide
        if current_slide_pointer == len(self._slides):
            return self._current_slide()

        # If it's one before the last
        if current_slide_pointer == len(self._slides) - 1:
            self._next_slide = None
        else:
            self._next_slide = self._slides[current_slide_pointer + 1]

        self._current_slide()

    def previous(self):
        if self._previous_slide:
            self.__clear()
            self._next_slide = self._previous_slide
            return self.next()

    def _read_input(self):
        with raw_stdin():
            char = sys.stdin.read(1)

        return ord(char)

    def present(self):
        self.next()

        while True:
            key = self._read_input()

            if key in PREV_KEYS:
                self.previous()
            elif key in NEXT_KEYS:
                self.next()
            elif key == INTERRUPT:
                return
