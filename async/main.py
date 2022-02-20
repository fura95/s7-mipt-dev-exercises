import asyncio

import time

from lib.af import log, input_queue, process_input_1, process_input_2, process_input_3, final_process
from lib import sf



async def naive_solution():
    '''Асинхронный вариант (медленный)'''
    t1 = time.time()
    await log('Starting naive solution')
    async for i in input_queue():
        p1 = await process_input_1(i)
        p2 = await process_input_2(i)
        p3 = await process_input_3(i)
        f = await final_process(p1, p2, p3)
        await log(f'{i}: {f}')
    await log(f'Total_time(naive solution): {time.time() - t1}')


def sync_solution():
    '''Последовательное/синхронное решение'''
    t1 = time.time()
    sf.log('Starting sync solution') 
    for i in sf.input_queue():
        p1 = sf.process_input_1(i)
        p2 = sf.process_input_2(i)
        p3 = sf.process_input_3(i)
        f = sf.final_process(p1, p2, p3)
        sf.log(f'{i}: {f}')
    sf.log(f'Total_time (sync solution): {time.time() - t1}')


if __name__ == '__main__':
    sync_solution()
    asyncio.run(naive_solution()) # всегда ждет и последовательно выполяется
    #asyncio.run(naive_solution_var1())
    #asyncio.run(naive_solution_var2())
