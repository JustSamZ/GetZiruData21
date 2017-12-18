import asyncio
import time
from aiohttp import ClientSession
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
my_set = db.ziru_SH1218

#all_url = ['http://sh.ziroom.com/z/vr/60746029.html','http://sh.ziroom.com/z/vr/60798323.html','http://sh.ziroom.com/z/vr/60878247.html','http://sh.ziroom.com/z/vr/60781346.html']
all_url = function.get_url_all(starturl)


async def do_some_work(url):
    global RESPONSE_LIST
    async with ClientSession() as session:
        async with session.get(url) as response:
            return  await response.read()

start = now()


tasks = []
async def run():
    for i in range(0, 512):
        coroutinge = asyncio.ensure_future(do_some_work(all_url[i]))
        tasks.append(coroutinge)
        requestlist = await asyncio.gather(*tasks)

        print(len(requestlist))
    return requestlist
#requestlist = await asyncio.await(tasks)

    #print(i,all_url[i])
    #print(type(requestlist))
#print(type(responses))
#print(type(responses.result))

'''
        my_set.insert({
        "SN": function.GetRoomSn(requestlist),
        "Name": function.GetRoomName(requestlist),
        "price": function.GetRoomRent(requestlist),
        "area": function.GetRoomArea(requestlist),
        "Direction": function.GetRoomDirection(requestlist),
        "Model": function.GetRoomModel(requestlist),
        "Floor": function.GetRoomFloor(requestlist),
        "SubLine": function.GetLocLine(requestlist),
        "Distance": function.GetDistance(requestlist),
        "CoorDinate": function.GetCoorDinate(requestlist),
        "RoomMateInfo": function.GetRoomMateInfo(requestlist),
        "pageurl": all_url[i],  # this need test first.

    })
'''
    #print('done')
start = now()


async def write():
        for i in range(0, 512):
            requestlist = run()
            my_set.insert({
        "SN": function.GetRoomSn(requestlist),
        "Name": function.GetRoomName(requestlist),
        "price": function.GetRoomRent(requestlist),
        "area": function.GetRoomArea(requestlist),
        "Direction": function.GetRoomDirection(requestlist),
        "Model": function.GetRoomModel(requestlist),
        "Floor": function.GetRoomFloor(requestlist),
        "SubLine": function.GetLocLine(requestlist),
        "Distance": function.GetDistance(requestlist),
        "CoorDinate": function.GetCoorDinate(requestlist),
        "RoomMateInfo": function.GetRoomMateInfo(requestlist),
        "pageurl": all_url[i],  # this need test first.

    })


loop = asyncio.get_event_loop()
future = asyncio.ensure_future(write())
loop.run_until_complete(future)

print('TIME: ', now() - start)



