
from pymongo import MongoClient
import redis
#starturl:Start on this page. start url list:

starturl = 'http://sh.ziroom.com/z/nl/z2.html?qwd=&p=1' #shanghai
#starturl = 'http://sz.ziroom.com/z/nl/z3.html?p=3'  #shengzhen








#database: mongodb

conn = MongoClient('localhost', 27017)
db = conn.ziru
my_set = db.ziru_SH1216

#database : redis:
r = redis.Redis(host='192.168.2.200', port=6379, decode_responses=True)