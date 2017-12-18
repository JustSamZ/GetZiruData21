import asyncio
import time
from aiohttp import ClientSession
import requests
from pymongo import MongoClient
import fun

now = lambda: time.time()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
start = requests.get(url='http://sh.ziroom.com/z/nl/z2.html?qwd=&p=1', headers=headers)
starturl = 'http://sh.ziroom.com/z/nl/z2.html?qwd=&p=1' #shanghai
conn = MongoClient('localhost', 27017)
db = conn.ziru
my_set = db.ziru_SH1216

#all_url = ['http://sh.ziroom.com/z/vr/60746029.html','http://sh.ziroom.com/z/vr/60798323.html','http://sh.ziroom.com/z/vr/60878247.html','http://sh.ziroom.com/z/vr/60781346.html']
all_url = fun.get_url_all(starturl)
''''''


async def get_response(url):
    async with ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            response = await response.text()
            return response


async def run(url_list):
    start = time.time() #计时
    tasks = []
    response_list = []

    for i in range(200):
        print(url_list[i])
        task = asyncio.ensure_future(get_response(url_list[i]))
        tasks.append(task)
    responses = await asyncio.gather(*tasks)
    response_list.append(responses)
    response_list = response_list[0]
        # you now have all response bodies in this variable
    end = time.time()
    print('Send TIME: ', end - start)

    print(len(response_list))


    start = time.time()  # 计时

    for j in range(len(response_list)):
        #print(j,'len:',len(response_list))
        print(fun.GetRoomSn(str(response_list[j])))
        #print(response_list[j])
        #print(fun.GetRoomName(str(response_list[j])))
        print(fun.GetRoomRent(str(response_list[j])))
        #print(fun.GetRoomRent(response_list[i]))


    end = time.time()
    print('Processing TIME: ', end - start)
    '''

    for i in range(len(response_list)):
        my_set.insert({
            "SN": fun.GetRoomSn(response_list[i]),
            "Name": fun.GetRoomName(response_list[i]),
            "price": fun.GetRoomRent(response_list[i]),
            "area": fun.GetRoomArea(response_list[i]),
            "Direction": fun.GetRoomDirection(response_list[i]),
            "Model": fun.GetRoomModel(response_list[i]),
            "Floor": fun.GetRoomFloor(response_list[i]),
            "SubLine": fun.GetLocLine(response_list[i]),
            "Distance": fun.GetDistance(response_list[i]),
            "CoorDinate": fun.GetCoorDinate(response_list[i]),
            "RoomMateInfo": fun.GetRoomMateInfo(response_list[i]),
            "pageurl": all_url[i],  # this need test first.

        })
    '''


start = now()

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(all_url))
loop.run_until_complete(future)
#loop.run_until_complete(asyncio.wait(tasks))
print('TIME: ', now() - start)



