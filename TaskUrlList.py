# Create in 2017-12-19
import Setting
import fun
import time
starturl = Setting.starturl

all_url = fun.get_url_all(starturl)

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
print(split_list(all_url,500))
end = time.time()
print('TIME: ', end - start)
'''
split_all_url = split_list(all_url,500)
