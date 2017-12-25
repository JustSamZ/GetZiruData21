


list1 = ['asd','1231','14123','ojkjhh']

'''
with open('test1.txt','a') as f:
    try:
        for i in range(len(list1)):
            f.write(list1[i]+'\n')
    finally:
        f.close()

'''
with open('test1.txt','r') as f:
    list2 = []
    list3 = []
    try:
        list2 = f.readlines()
        for i in range(len(list2)):
            list3.append(list2[i].rstrip('\n'))
    finally:
        f.close()


    print(list2)
    print(list3)
    print(len(list3))