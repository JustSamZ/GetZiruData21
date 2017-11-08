import requests
import re
import function
import time
from pymongo import MongoClient
import function

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
start = requests.get(url='http://sh.ziroom.com/z/nl/z2.html?qwd=&p=1', headers=headers)
#starturl = 'http://sh.ziroom.com/z/nl/z2.html?qwd=&p=1' #shanghai
starturl = 'http://sz.ziroom.com/z/nl/z3.html?p=3'  #shengzhen

# mongo connection:

conn = MongoClient('localhost', 27017)
db = conn.mydb
# my_set = db.ziroom
# my_set = db.url_list
my_set = db.ziru_SZ_data900_9_1

if __name__ == "__main__":
    # listtest = function.get_url_all(start)
    # function.get_url_all(starturl)
    # print(listtest)
    # my_set.insert({"URL":function.get_url_all(starturl)})
    all_url = []
    all_url = function.get_url_all(starturl)
    for i in range(0, len(all_url)):  #
        start = time.time()  # 计时
        requestlist = requests.get(url=all_url[i], headers=headers)

        # 1print(function.GetRoomSn(requestlist)) #pass
        print(all_url[i], i, 'start')
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

        end = time.time()
        # print(end - start)
        print('done，spend time:', end - start)

        # my_set.insert(insert)



        # 2print(function.GetRoomName(requestlist))  #pass


        # 3print(function.GetRoomRent(requestlist))  #pass



        # 8print(function.GetLocLine(requestlist)) #pass


        # 4print(function.GetRoomArea(requestlist)) # pass


        # 5print(function.GetRoomDirection(requestlist)) # pass



        # 6print(function.GetRoomModel(requestlist)) #pass


        # 7print(function.GetRoomFloor(requestlist)) #pass

        # 9print(function.GetDistance(requestlist))  #pass



        # 10print(function.GetCoorDinate(requestlist)) #pass

        # print(function.GetRoomPic(requestlist)) # failed

        # 11print(function.GetRoomMateInfo(requestlist)) #pass







