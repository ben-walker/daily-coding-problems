'''
Implement a job scheduler which takes in a function f and an integer n, and
calls f after n milliseconds.
'''

import asyncio


def to_sec(ms):
    return ms / 1000

async def job_scheduler(f, n):
    await asyncio.sleep(to_sec(n))
    f()

asyncio.run(job_scheduler(print, 500))
