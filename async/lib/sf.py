"""
Синхронный набор функций
"""

import math
from typing import Any, Generator, Iterable
import time

SLEEP_TIME = 1


def log(value: Any):
    '''Ожидание и запись логов'''
    time.sleep(SLEEP_TIME)
    print(value)


def input_queue() -> Iterable[int]:
    '''Ожидание и выдается число'''
    for i in range(3):
        time.sleep(SLEEP_TIME)
        yield i


def process_input_1(i: int) -> int:
    '''Произвольная функция'''
    time.sleep(SLEEP_TIME)
    return i ** 2


def process_input_2(i: int) -> int:
    '''Произвольная функция'''
    time.sleep(SLEEP_TIME)
    return i ** 3


def process_input_3(i: int) -> int:
    '''Произвольная функция'''
    time.sleep(1)
    return int(math.sqrt(i))


def final_process(p1: int, p2: int, p3: int) -> int:
    '''Результат других функций'''
    time.sleep(SLEEP_TIME)
    return p1 + p2 + p3
