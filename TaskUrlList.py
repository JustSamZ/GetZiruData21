# Create in 2017-12-19
import Setting
import fun
starturl = Setting.starturl

#all_url = fun.get_url_all(starturl)


#将爬好的目标url全部存入文件中，下次调用直接从文件中取得。
def Geturl_infile():
    urllist = fun.get_url_all(starturl)
    with open('taskurl1226.txt', 'a') as f:
        try:
            for i in range(len(urllist)):
                f.write(urllist[i]+'\n')
        finally:
            f.close()

#Geturl_infile()


#调用该函数 将返回 所用任务的url list
def Geturl_fromfile():
    with open('taskurl1226test1.txt', 'r') as f:
        #list2 = []
        list3 = []
        try:
            list2 = f.readlines()
            for i in range(len(list2)):
                list3.append(list2[i].rstrip('\n'))
        finally:
            f.close()

        return list3
#Geturl_fromfile()



# list 拆分成小list.  参数分别是： 大列表，每份元素个数。 返回拆分后的列表。list = [1,2,3,4,5,6,7,8,9,0] > [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]
def split_list(list, num):
    if len(list) > num:
        newlist = []
        a = (len(list)//num)
        for i in range(a):
            newlist.append(list[num*i :num*(i+1)])
        last = divmod(len(list),num)[1]
        if last != 0:
            newlist.append(list[a*num : ])
        return newlist

    else:
        print('error')

'''
# test function:
list = [1,2,3,4,5,6,7,8,9,0]
start = time.time()
print(len(split_list(all_url,500)))
end = time.time()
print('TIME: ', end - start)
'''
#split_all_url = split_list(all_url,500)
