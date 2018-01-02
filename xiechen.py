import asyncio
import time
import multiprocessing
from aiohttp import ClientSession
import Setting
import Header_UA_Cookies
import TaskUrlList
r = Setting.r

headers = Header_UA_Cookies.headers
starturl = Setting.starturl
my_set = Setting.my_set

start = time.time() #计时

all_url = TaskUrlList.Geturl_fromfile()
#print('total url:' ,len(all_url))
all_url = TaskUrlList.split_list(all_url,500)
#print('total num:',len(all_url))
#print('total num:',len(all_url[18]))
#print(all_url[18])


end = time.time()
#print('get url TIME: ', end - start)




async def get_response(url):
    # asyncio.Semaphore(),限制同时运行协程数量
    sem = asyncio.Semaphore(500)
    with (await sem):
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


    '''
    for i in range(len(response_list)):
        r.rpush('list2', response_list[i])
    print(r.llen('list2'))
    '''
    # print(len(list1))
    # for i in range(len(list1)):
    #    r.rpush('list1',list1[i])
    # r.rpush('list1',list1[1])
    #print(r.llen('list1'))
    # print(r.lrange('list1',0,100))
    # r.delete('list1')


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


def asyloop(url):
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(url))
    loop.run_until_complete(future)


if __name__ == "__main__":

    start = time.time()

    pool = multiprocessing.Pool(processes=8)
    result = []
    print('rand:',len(all_url))
    for i in range(len(all_url)):
        result.append(pool.apply_async(asyloop, (all_url[i],)))
        print('loop:', i)
        time.sleep(5)
    pool.close()
    pool.join()
    for res in result:
        print("every time:", res, res.get())
    end = time.time()
    print('Processing Total TIME: ', end - start)
    print(len(result), "Sub-process(es) done.")


