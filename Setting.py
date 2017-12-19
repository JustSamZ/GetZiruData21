
from pymongo import MongoClient

#starturl:Start on this page. start url list:

starturl = 'http://sh.ziroom.com/z/nl/z2.html?qwd=&p=1' #shanghai
#starturl = 'http://sz.ziroom.com/z/nl/z3.html?p=3'  #shengzhen








#database: mongodb

conn = MongoClient('localhost', 27017)
db = conn.ziru
my_set = db.ziru_SH1216