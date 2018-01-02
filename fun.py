import requests
import re
import Header_UA_Cookies
headers = Header_UA_Cookies.headers

#T_GetRoomCheckInData = re.compile(r'(<p>\s*20[1-2][0-9]\/[0-1][0-9]-20[1-2][0-9]\/[0-1][0-9]<\/p>)')  # remove
#T_GetRoomNum = re.compile(r'(<p>0[1-9]卧<\/p>)')  # remove
#T_GetRooMateInfo = re.compile(r'(<div\sclass="user_top\sclearfix">(\s*.*){1,13})')

def every_page_urllist(startpage):
    geturl1 = re.compile(r'(<h3><a.*?f=".*?\.html")')
    geturl2 = re.compile(r'(hr.*?\/.*?\.html)')
    urltab = geturl1.findall(startpage.text)
    url1 = geturl2.findall(str(urltab))
    url2 = []
    for i in range(0, len(url1)):
        url2.append(url1[i].replace('href="', 'http:'))
    return url2

def get_nextpage_url(startpage):
    geturlTab = re.compile(r'(<a\sclass="next".*?href=".*?")')
    get_nextpage_url = re.compile(r'(hr.*?\/.*=\d+)')
    urltab = geturlTab.findall(startpage.text)[0]
    url1 = get_nextpage_url.findall(str(urltab))
    url2 = []
    url2.append(url1[0].replace('href="', 'http:'))
    return url2[0]

def get_url_all(starturl):
    all_url = []
    all_url_task = []

    for i in range(1, 51):
        pageurl = starturl[:-1] + str(i)
        startpage = requests.get(url=pageurl, headers=headers)
        a = every_page_urllist(startpage)
        all_url.append(a)
    # 下面我要压平二维列表：
    for i in range(len(all_url)):
        for j in range(len(all_url[i])):
            all_url_task.append(all_url[i][j])
    all_url_task = list(set(all_url_task))  # 去重复
    return all_url_task

#for async, remove all .text by sam 20171218
def GetRoomSn(Html_Response):
    T_GetSn = re.compile(r'("SH\w\w(\w|\d|_)*")')
    GetSn = re.compile(r'(SH\w{1,50})')
    SnWithTab = T_GetSn.findall(Html_Response)
    Sn = GetSn.findall(str(SnWithTab))
    return Sn


def GetRoomName(Html_Response):
    T_GetRoomName = re.compile(r'([^\x00-\xff]*[0-9]*[^\x00-\xff]*.*[0-9]*[^\x00-\xff])') #old: <h2>\s*[^\x00-\xff]*\d*[^\x00-\xff]*-\d*[^\x00-\xff]*\s*<\/h2> new:<h2>\s*[^\x00-\xff]*\d*[^\x00-\xff]*.*\s*<\/h2>
    GetRoomName = re.compile(r'([^\x00-\xff]*[0-9]*[^\x00-\xff]*[0-9]*[^\x00-\xff]*-0[0-9][^\x00-\xff])') #old:[^\x00-\xff]*[0-9][^\x00-\xff]*-0[0-9][^\x00-\xff]  new: [^\x00-\xff]*[0-9][^\x00-\xff]*.*0[0-9][^\x00-\xff]
    RoomNameWithTab = T_GetRoomName.findall(Html_Response)
    RoomName = GetRoomName.findall(str(RoomNameWithTab))
    return RoomName


def GetRoomRent(Html_Response):
    T_GetRoomRent = re.compile(r'(<span class="room_price" id="room_price">￥\d+<\/span>)')
    GetRoomRent = re.compile(r'(￥\d{1,5})')
    RoomRentWithTab = T_GetRoomRent.findall(Html_Response)
    RoomRent = GetRoomRent.findall(str(RoomRentWithTab))
    return RoomRent


def GetLocLine(Html_Response):
    T_GetLocLine = re.compile(r'(<span class="ellipsis">\s*\[.+\s*.*<\/span>)')
    GetLocLine = re.compile(r'(\d{0,1}[\u4e00-\u9fa5]{1,20})')
    LocLineWithTab = T_GetLocLine.findall(Html_Response)
    LocLine = GetLocLine.findall(str(LocLineWithTab))
    return LocLine


def GetRoomArea(Html_Response):
    T_GetRoomArea = re.compile(r'(<li>.*?面积：\s*.*?[0-9]+([.]{1}[0-9]+){0,1}\s*㎡<\/li>)')
    GetRoomArea = re.compile(r'([0-9]+([.]{1}[0-9]+){0,1})')
    RoomAreaWithTab = T_GetRoomArea.findall(Html_Response)
    RoomArea = GetRoomArea.search(str(RoomAreaWithTab))
    return (RoomArea.group(0) + '㎡')


def GetRoomDirection(Html_Response):
    T_GetRoomDirection = re.compile(r'(<li><b><\/b>.*[南|北|东|西]<\/li>)')
    GetRoomDirection = re.compile(r'(朝向|东|南|西|北)')
    RoomDirectionWithTab = T_GetRoomDirection.findall(Html_Response)
    RoomDirection = GetRoomDirection.findall(str(RoomDirectionWithTab))
    return RoomDirection


def GetRoomModel(Html_Response):
    T_GetRoomModel = re.compile(r'(<li><b><\/b>.*\d室\d厅\s*<span class="icons">[\u4e00-\u9fa5]<\/span>\s*<\/li>)')
    GetRoomModel = re.compile(r'(户型：|\d室\d厅)')
    GetRoomModelWithTab = T_GetRoomModel.findall(Html_Response)
    RoomModel = GetRoomModel.findall(str(GetRoomModelWithTab))
    return RoomModel


def GetRoomFloor(Html_Response):
    T_GetRoomFloor = re.compile(r'(<li><b><\/b>楼层.{1,100}<\/li>)')
    GetRoomFloor = re.compile(r'(楼层：|\d{1,3}\/\d{1,2}层)')
    GetRoomFloorWithTab = T_GetRoomFloor.findall(Html_Response)
    RoomFloor = GetRoomFloor.findall(str(GetRoomFloorWithTab))
    return RoomFloor


def GetDistance(Html_Response):
    T_GetDistance = re.compile(r'(<b><\/b>交通.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n)')
    GetDistance = re.compile(r'(距|\d号线[^\x00-\xff]*\d{1,4}米)')
    GetDistanceWithTab = T_GetDistance.findall(Html_Response)
    Distance = GetDistance.findall(str(GetDistanceWithTab))
    return Distance


def GetCoorDinate(Html_Response):
    T_GetRoomCoordinate = re.compile(r'(data-lng="\d{1,3}\.\d+"|data-lat="\d{1,2}\.\d+")')
    CoorDinate = T_GetRoomCoordinate.findall(Html_Response)
    return CoorDinate


def GetRoomPic(Html_Response):
    T_GetRoomPic = re.compile(r'(<a\shref="http:\/\/.*\.(JPG|jpg)"\s*class="pirobox_t6">)')
    GetRoomPic = re.compile(r'(http:\/\/pic\.ziroom\.com(\/(\w|\d|_|-)+)+\.jpg|JPG)')
    GetRoomPicWithTab = T_GetRoomPic.findall(Html_Response)
    RoomPic_Du = GetRoomPic.findall(str(GetRoomPicWithTab))
    RoomPic = list(set(RoomPic_Du))  # remove duplicate

    # get the url of pic from tup
    RoomPicList = []
    for i in range(0, len(RoomPic)):
        RoomPicList.append((RoomPic[i])[0])
    return print(RoomPicList)


def GetRoomMateInfo(Html_Response):
    T_GetRooMateInfo = re.compile(r'(<div\sclass="user_top\sclearfix">(\s*.*){1,13})')
    GetRoomMateInfo1 = re.compile(r'(\d\d卧)')
    GetRoomMateInfo2 = re.compile(r'(当前房源|已入住|可入住|配置中)')
    GetRoomMateInfo3 = re.compile(r'([\u4e00-\u9fa5]{2}座)')
    GetRoomMateInfo4 = re.compile(r'((woman)|(man))')
    GetRoomMateInfo5 = re.compile(r'(20[1-2][0-9]\/[0-1][0-9]-20[1-2][0-9]\/[0-1][0-9])')
    GetRoomMateInfoWithTab = T_GetRooMateInfo.findall(Html_Response.text)
    RoomMateInfo1 = GetRoomMateInfo1.findall(str(GetRoomMateInfoWithTab))
    RoomMateInfo2 = GetRoomMateInfo2.findall(str(GetRoomMateInfoWithTab))
    RoomMateInfo3 = GetRoomMateInfo3.findall(str(GetRoomMateInfoWithTab))
    RoomMateInfo4_1 = GetRoomMateInfo4.findall(Html_Response)
    RoomMateInfo5 = GetRoomMateInfo5.findall(str(GetRoomMateInfoWithTab))

    # remove duplicate 'woman or man'from findall
    RoomMateInfo4 = []

    for i in range(0, len(RoomMateInfo4_1)):
        RoomMateInfo4.append(RoomMateInfo4_1[i][0])

    RoomUser = []

    for i in range(0, len(RoomMateInfo1)):
        if (RoomMateInfo2[i] == '可入住' or RoomMateInfo2[i] == '当前房源' or RoomMateInfo2[i] == '配置中'):
            RoomMateInfo2[i] = '空置'
            RoomMateInfo3.insert(i, '无人')
            RoomMateInfo4.insert(i, '无性别')
            RoomMateInfo5.insert(i, '无入住时间')
        RoomUser.append(RoomMateInfo1[i])
        RoomUser.append(RoomMateInfo2[i])
        try:
            RoomUser.append(RoomMateInfo3[i])
            RoomUser.append(RoomMateInfo4[i])
            RoomUser.append(RoomMateInfo5[i])
        except IndexError:
            RoomUser.extend(['无人', '无性别', '无入住时间'])
    return RoomUser


