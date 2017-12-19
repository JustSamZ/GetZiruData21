import asyncio
import time
from aiohttp import ClientSession
import fun
import Setting
import Header_UA_Cookies
import TaskUrlList

headers = Header_UA_Cookies.headers
starturl = Setting.starturl
my_set = Setting.my_set

#all_url = ['http://sh.ziroom.com/z/vr/60746029.html','http://sh.ziroom.com/z/vr/60798323.html','http://sh.ziroom.com/z/vr/60878247.html','http://sh.ziroom.com/z/vr/60781346.html']
all_url = TaskUrlList.split_all_url
print(len(all_url[1]))

async def get_response(url):
        async with ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                response = await response.text()
                return response

async def run(url_list):
    start = time.time() #计时
    tasks = []
    response_list = []

    for i in range(len(all_url[1])):
        #print(url_list[i])
        task = asyncio.ensure_future(get_response(all_url[1][i]))
        tasks.append(task)
    end = time.time()
    print('Send TIME1: ', end - start)
    responses = await asyncio.gather(*tasks)
    response_list.append(responses)
    response_list = response_list[0]# you now have all response bodies in this variable
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

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(all_url[1]))
loop.run_until_complete(future)


