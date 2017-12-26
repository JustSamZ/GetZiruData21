import asyncio
import time
from aiohttp import ClientSession
import fun
import Setting
import Header_UA_Cookies
import TaskUrlList
import redis
r = redis.Redis(host='192.168.2.200', port=6379, decode_responses=True)

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
    #将response 内容写入redis 中的list1 里。分片此次写入400条

    for i in range(len(response_list)):
        r.rpush('list2', response_list[i])
    print(r.llen('list2'))

    # print(len(list1))
    # for i in range(len(list1)):
    #    r.rpush('list1',list1[i])
    # r.rpush('list1',list1[1])
    #print(r.llen('list1'))
    # print(r.lrange('list1',0,100))
    # r.delete('list1')

    start = time.time()  # 计时
    '''
    for j in range(len(response_list)):
        print(j , 'start:')
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
    '''
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(all_url[1]))
loop.run_until_complete(future)


