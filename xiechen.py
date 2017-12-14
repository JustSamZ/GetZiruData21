import asyncio
import time

import requests
import re
import function
from pymongo import MongoClient
import function

now = lambda: time.time()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
start = requests.get(url='http://sh.ziroom.com/z/nl/z2.html?qwd=&p=1', headers=headers)
starturl = 'http://sh.ziroom.com/z/nl/z2.html?qwd=&p=1' #shanghai
conn = MongoClient('localhost', 27017)
db = conn.ziru
my_set = db.ziru_SH1224

all_url = ['http://sh.ziroom.com/z/vr/60746029.html','http://sh.ziroom.com/z/vr/60798323.html','http://sh.ziroom.com/z/vr/60878247.html','http://sh.ziroom.com/z/vr/60781346.html']
#all_url = function.get_url_all(starturl)


async def do_some_work(i):
    requestlist = await requests.get(url=all_url[i], headers=headers)
    return 'Done after:'

async def main():
    tasks = []
    for i in range(0, len(all_url)):
        tasks.append(asyncio.ensure_future(do_some_work(i)))

    dones, pendings = await asyncio.wait(tasks)

    for task in dones:
        print('Task ret: ', task.result())
start = now()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print('TIME: ', now() - start)



