import asyncio

import time

from lib.af import log, input_queue, process_input_1, process_input_2, process_input_3, final_process
from lib import sf



async def naive_solution():
    t1 = time.time()
    await log('Starting')
    async for i in input_queue():
        p1 = await process_input_1(i)
        p2 = await process_input_2(i)
        p3 = await process_input_3(i)
        f = await final_process(p1, p2, p3)
        await log(f'{i}: {f}')
    await log(f'Total_time: {time.time() - t1}')


def sync_solution():
    t1 = time.time()
    sf.log('Starting')
    for i in sf.input_queue():
        p1 = sf.process_input_1(i)
        p2 = sf.process_input_2(i)
        p3 = sf.process_input_3(i)
        f = sf.final_process(p1, p2, p3)
        sf.log(f'{i}: {f}')
    sf.log(f'Total_time: {time.time() - t1}')


async def foo(i):
    p1, p2, p3 = await asyncio.gather(
        process_input_1(i),
        process_input_2(i),
        process_input_3(i)
    )
    f = await final_process(p1, p2, p3)
    asyncio.ensure_future(log(f'{i}: {f}'))


async def my_solution():
    t1 = time.time()
    q = asyncio.create_task(log('Starting'))
    tasks = []
    async for i in input_queue():
        tasks.append(asyncio.create_task(foo(i)))
    await asyncio.gather(*tasks)
    await log(f'Total_time: {time.time() - t1}')



if __name__ == '__main__':
    # sync_solution()


    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(my_solution())
    finally:
        loop.close()

    # asyncio.run(naive_solution())

    asyncio.run(my_solution())
