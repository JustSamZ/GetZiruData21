import redis
import fun
import time
r = redis.Redis(host='192.168.2.200', port=6379, decode_responses=True)
#r.set('name','teesssst')

list1 = ['http://sh.ziroom.com/z/vr/60746029.html','http://sh.ziroom.com/z/vr/60798323.html','http://sh.ziroom.com/z/vr/60878247.html','http://sh.ziroom.com/z/vr/60781346.html']
#print(len(list1))
#for i in range(len(list1)):
#    r.rpush('list1',list1[i])
#r.rpush('list1',list1[1])
print(r.llen('list1'))
#print(r.lrange('list1',0,100))
#r.delete('list1')

response_list = r.lrange('list1',0,900)
print(len(response_list))
start = time.time()  # 计时



for j in range(len(response_list)):
    print(j, 'start:')
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
    # print(fun.GetRoomMateInfo(str(response_list[j])))

end = time.time()
print('Processing TIME: ', end - start)
