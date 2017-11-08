import re
from pymongo import MongoClient
conn = MongoClient('localhost', 27017)
db = conn.mydb
collection = db.ziru_data900_2017_8_32
price_org = collection.find({}, {"price": 1})
area = collection.find({}, {"area": 1})

def data_clear_rm_id(list): #
    list1 = []
    for key in list:
        del key["_id"]
        list1.append(key)
    return list1

def data_clear_rm_onlynum(list):
    list2 = []
    for i in range(0, len(list)):
        for value in list[i]:
            mid = re.findall(r'\d+', str(list[i][value]))
            list2.append(float(mid[0]))
    return list2

price1 = data_clear_rm_id(price_org)
print(price1)
'''
print(str(price[0]))
mid = re.findall(r'\d+', str(price[0]))
print(float(str(mid[0])))
'''
price_onlynum = data_clear_rm_onlynum(price1)
print(len(price1))
print(price_onlynum)

area1 = data_clear_rm_id(area)
area_onlynum = data_clear_rm_onlynum(area1)
print(len(area1))
#print(area_onlynum)
price_area = []

#price_area1 = [[price_onlynum[1]][area_onlynum[1]]]
if len(price1) == len(area1):
    for i in range(0, len(price1)):
        #print(i)
        price_area.append([price_onlynum[i], area_onlynum[i]])


print(price_area)