import time
from typing import Callable

class Foo:
    def __init__(self):
        self.flag = ""

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.flag = "first"

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        while self.flag != "first":
            time.sleep(0.01)
        printSecond()
        self.flag = "second"

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        while self.flag != "second":
            time.sleep(0.01)
        printThird()
