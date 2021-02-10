import asyncio
import math
from typing import AsyncIterable, Any

SLEEP_TIME = 1


async def log(value: Any):
    await asyncio.sleep(SLEEP_TIME)
    print(value)


async def input_queue() -> AsyncIterable[int]:
    for i in range(3):
        await asyncio.sleep(SLEEP_TIME)
        yield i


async def process_input_1(i: int) -> int:
    await asyncio.sleep(SLEEP_TIME)
    return i ** 2


async def process_input_2(i: int) -> int:
    await asyncio.sleep(SLEEP_TIME)
    return i ** 3


async def process_input_3(i: int) -> int:
    await asyncio.sleep(1)
    return int(math.sqrt(SLEEP_TIME))


async def final_process(p1: int, p2: int, p3: int) -> int:
    await asyncio.sleep(SLEEP_TIME)
    return p1 + p2 + p3
