import multiprocessing
import redis
import fun
import time
r = redis.Redis(host='192.168.2.200', port=6379, decode_responses=True)


def func(response_list):
    start = time.time()
    #for j in range(len(response_list)):
    #print(j, 'start:')
    print(fun.GetRoomSn(str(response_list)))
    print(fun.GetRoomName(str(response_list)))
    print(fun.GetRoomRent(str(response_list)))
    print(fun.GetRoomArea(str(response_list)))
    print(fun.GetRoomDirection(str(response_list)))
    print(fun.GetRoomModel(str(response_list)))
    print(fun.GetRoomFloor(str(response_list)))
    print(fun.GetLocLine(str(response_list)))
    print(fun.GetDistance(str(response_list)))
    print(fun.GetCoorDinate(str(response_list)))
    # print(fun.GetRoomMateInfo(str(response_list[j])))
    end = time.time()
    return end - start


if __name__ == "__main__":

    response_list = r.lrange('list1', 0, 900)
    print(len(response_list))
    start = time.time()

    pool = multiprocessing.Pool(processes=8)
    result = []
    for i in range(len(response_list)):
        #msg = "hello %d" % (i)
        result.append(pool.apply_async(func, (response_list[i],)))
    pool.close()
    pool.join()
    for res in result:
        print("every time:", res.get())
    end = time.time()
    print('Processing Total TIME: ', end - start)
    print(len(result), "Sub-process(es) done.")
