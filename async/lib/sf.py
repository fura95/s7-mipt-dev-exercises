import math
from typing import Any, Generator, Iterable
import time

SLEEP_TIME = 1


def log(value: Any):
    time.sleep(SLEEP_TIME)
    print(value)


def input_queue() -> Iterable[int]:
    for i in range(3):
        time.sleep(SLEEP_TIME)
        yield i


def process_input_1(i: int) -> int:
    time.sleep(SLEEP_TIME)
    return i ** 2


def process_input_2(i: int) -> int:
    time.sleep(SLEEP_TIME)
    return i ** 3


def process_input_3(i: int) -> int:
    time.sleep(1)
    return int(math.sqrt(SLEEP_TIME))


def final_process(p1: int, p2: int, p3: int) -> int:
    time.sleep(SLEEP_TIME)
    return p1 + p2 + p3
