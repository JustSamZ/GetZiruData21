
import asyncio
import aiohttp
import time
from aiohttp import ClientSession
import requests
from pymongo import MongoClient
import fun

NUMBERS = range(12)
URL = 'http://httpbin.org/get?a={}'

sema = asyncio.Semaphore(3)  # global nonlocal


async def fetch_async(a):
    async with aiohttp.get(URL.format(a)) as r:
        data = await r.json()
    return data['args']['a']


async def print_result(a):
    with (await sema):
        r = await fetch_async(a)
        print('fetch({}) = {}'.format(a, r))


loop = asyncio.get_event_loop()
f = asyncio.wait([print_result(num) for num in NUMBERS])
loop.run_until_complete(f)
loop.close()