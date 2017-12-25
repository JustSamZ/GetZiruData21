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

start = time.time() #计时

all_url = TaskUrlList.Geturl_fromfile()
all_url = TaskUrlList.split_list(all_url,500)

end = time.time()
print('get url TIME: ', end - start)
#all_url2 = fun.get_url_all(starturl)



async def get_response(url):
        async with ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                response = await response.text()
                return response

async def run(url_list):
    start = time.time() #计时
    tasks = []
    response_list = []

    for i in range(len(url_list)):
        #print(url_list[i])
        task = asyncio.ensure_future(get_response(url_list[i]))
        tasks.append(task)
    end = time.time()
    print('Send TIME: ', end - start)
    responses = await asyncio.gather(*tasks)
    response_list.append(responses)
    response_list = response_list[0]# you now have all response bodies in this variable
    end = time.time()
    print('Get response TIME: ', end - start)
    print(len(response_list))
    start = time.time()  # 计时

    for j in range(len(response_list)):

        print(fun.GetRoomSn(str(response_list[j])))
        print(fun.GetRoomName(str(response_list[j])))
        print(fun.GetRoomRent(str(response_list[j])))
        print(fun.GetRoomArea(str(response_list[j])))
        print(fun.GetRoomDirection(str(response_list[j])))
        print(fun.GetRoomModel(str(response_list[j])))
        print(fun.GetRoomFloor(str(response_list[j])))
        print(fun.GetLocLine(str(response_list[j])))
        print(fun.GetDistance(str(response_list[j])))
        print(fun.GetCoorDinate(str(response_list[j])))
        #print(fun.GetRoomMateInfo(str(response_list[j])))

    end = time.time()
    print('Processing TIME: ', end - start)

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(all_url[1]))
loop.run_until_complete(future)


