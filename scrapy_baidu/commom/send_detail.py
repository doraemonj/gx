import requests
import json, random, time

import pymongo

# 建立连接
client = pymongo.MongoClient('localhost', 27017)

# 连接数据库
db = client['test_db']

# 建立集合
collection = db['test_collection']

# 连接mysql服务器
import mysql.connector

# 连接数据库
conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = '12345678',
                       db = 'test1',
                       charset = 'utf8mb4',
                       cursorclass = pymysql.cursors.DictCursor)

#获取user token
from scrapy_baidu.commom.news_mysql import update_errflag, update_wberrflag

user_url = "https://laiteinfo.com/gx_manager/manager/crawler/login?"
params = {
    "username": "crawler",
    "password": "crawlerUU##999##112L"
}
res = requests.post(url=user_url, json=params)
result = res.json()
token = result.get('data')['token']
# print(token)
#
# #获取爬虫账号
header = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', # 设置完以后 传入的params对象就会时候用formdata传参的方式,
            'x-auth-token': token
            }
# scrapy_url = 'https://laiteinfo.com/gx_manager/mission/getPublishUsers'
#
get_user_id = 'https://laiteinfo.com/gx_manager/mission/getCrawlerPublishUsers'
# res = requests.post(url=scrapy_url, headers=headers)
res_user_id = requests.get(url=get_user_id, headers=header)
user_id_dic = res_user_id.json()
# print(user_id_dic)
user_list = user_id_dic.get('data')
# result = res.json()
# user_list = result.get('data')
# print(user_list)
user = [i.get('userId') for i in user_list]
# print(user,len(user))
# user = [10908, 10929, 10930, 10931, 10932, 10933, 10934, 10936, 27418, 10940, 10941, 10942, 10943, 10945, 10946, 10947, 10948, 15777, 15816, 15817, 15818, 15819, 15820, 15821, 15822, 15823, 15824, 16165, 16166, 16167, 16169, 16170, 16171, 16172, 16174, 16177, 16179, 16180, 16183, 16184, 16185, 16186, 16187, 16188, 16190, 16191, 16194, 16195, 16196, 16197, 16199, 16200, 16201, 16202, 37791, 37794, 37803, 37804, 37810, 37812, 37815, 37817, 37819, 37825, 37828, 37829, 37831, 37835, 37836, 37838, 37841, 37842, 49172, 49173, 49174, 49175, 49176, 49180, 49181, 49182, 49183, 17182, 49184, 49185, 17207]
# i = 48
# if i < len(user):
#     userid = user[i]
# else:
#     m = i%len(user)
#     print(m)
#     userid = user[m]
# print(userid)


#发送数据

url = "https://laiteinfo.com/mission/insert?x-auth-token=dd61641538a847778a315db06e0ad77f"
oss_url = "https://laiteinfo.com/user/oss/uploads"
oss_video_url = "https://laiteinfo.com/admin/vod/video/upload"
video_send_url = ""
pic_filePath = "D:\\pic_src"
video_filePath = "D:\\video_src"

# def pre(title, type, contentAttr, repeatId, hot, i):
#     print('type',type)
#     user = [i.get('userId') for i in user_list]
#     # userid = random.choice(user)
#     print('iiiiiiiiii',i)
#     print('len(user)',len(user))
#     if i < len(user):
#         userid = user[i]
#     else:
#         m = i%len(user)
#         print(m)
#         userid = user[m]
#     print(userid)
#     contentAttr = str(contentAttr).replace('text-align:  center', 'text-align:center')
#     headers = {'Content-Type': 'application/json'}
#     data = {
#              "type": "",
#              "isWaterMark": False,
#              "content": "",
#              "contentAttr": str(contentAttr),
#              "title": title,
#              "accessoryType": "",
#              "accessorys": [],
#              "lat": 31.30321580717796,
#              "lng": 120.59294231967466,
#              "location": "",
#              "topicName": [],
#              # "tagId": 19,
#              "tagId": int(type),
#              "status": 1,
#              "userId": userid,
#              "repeatId": repeatId
#              }
#     req = requests.post(url, data=json.dumps(data), headers=headers)  # 发post请求,以json字符串参数格式
#     print(req.text)
#     # if req.text == 'Method Not Allowed':
#     #     update_errflag(hot)
#     # print(json.loads(req.text))
#     print(userid, data.get('userId'))
#     # print(json.loads(req.text).get('code'))
#     if req.status_code != 200:
#         update_errflag(hot)
#     if json.loads(req.text).get('code'):
#         update_errflag(hot)
#     # return json.loads(req.text).get(data)[0]

def pre_luntan(title, type, contentAttr, repeatId, hot, i):
    print('type',type)
    user = [i.get('userId') for i in user_list]
    # userid = random.choice(user)
    print('iiiiiiiiii',i)
    print('len(user)',len(user))
    if i < len(user):
        userid = user[i]
    else:
        m = i%len(user)
        print(m)
        userid = user[m]
    print(userid)
    print('contentAttr',contentAttr)

    headers = {'Content-Type': 'application/json'}
    data = {
        "type": "",
        "isWaterMark": False,
        "content": "",
        "contentAttr": str(contentAttr),
        "title": title,
        "accessoryType": "",
        "accessorys": [],
        "lat": 31.30321580717796,
        "lng": 120.59294231967466,
        "location": "交通银行(苏州彩虹支行)",
        "topicName": [],
        "tagId": int(type),
        "status": 1,
        "userId": userid,
        "repeatId": repeatId
    }
    req = requests.post(url, data=json.dumps(data), headers=headers)  # 发post请求,以json字符串参数格式
    print(req.text)
    # if req.text == 'Method Not Allowed':
    #     update_errflag(hot)
    # print(json.loads(req.text))
    print(userid, data.get('userId'))
    # print(json.loads(req.text).get('code'))
    if req.status_code != 200:
        update_errflag(hot)
    if json.loads(req.text).get('code'):
        update_errflag(hot)
    # return json.loads(req.text).get(data)[0]

def oss_pic_pre(file_name, url):
    print(file_name,pic_filePath+'\\'+file_name)
    files = {'file': open(pic_filePath+'\\'+file_name, 'rb')}
    result = requests.post(oss_url, files=files)
    time.sleep(1)
    print(result.text)
    try:
        oss_path = json.loads(result.text).get('data')[0]
    except Exception as e:
        update_errflag(url)  # 更新flag,未保存div（后续处理）
        return 0
    print('oss_pathoss_pathoss_pathoss_path',oss_path,type(oss_path))
    return oss_path


# def wboss_pic_pre(file_name, mid):
#     print(file_name,pic_filePath+'\\'+file_name)
#     files = {'file': open(pic_filePath+'\\'+file_name, 'rb')}
#     result = requests.post(oss_url, files=files)
#     time.sleep(1)
#     print(result.text)
#     try:
#         oss_path = json.loads(result.text).get('data')[0]
#     except Exception as e:
#         # update_wberrflag(mid)  # 更新flag,未保存div（后续处理）
#         return 0
#     print('oss_pathoss_pathoss_pathoss_path',oss_path,type(oss_path))
#     return oss_path

# def oss_video_pre(file_name, url, video_filePath=video_filePath):
#     print(file_name, video_filePath+'\\'+file_name)
#     files = {'file': open(video_filePath+'\\'+file_name, 'rb')}
#     result = requests.post(oss_video_url, files=files)
#     print('video_result',result)
#     # result = '{"code":0,"message":"成功","data":["https://laitesprod.oss-cn-hangzhou.aliyuncs.com/somnus/2022/10/12/13aa6763-c0fe-4da8-85eb-96c6c03b46fc__1080*608.png"]}'
#     print(result.text)
#     try:
#         oss_path = json.loads(result.text).get('data')
#     except Exception as e:
#         # update_errflag(url)  # 更新flag,未保存div（后续处理）
#         return 0
#     print('oss_path', oss_path)
#     return oss_path

# insert_video_url = 'https://laiteinfo.com/video/upload'
# def video_send(title, video_url, repeatid, tagId, i):
#     headers = {
#         'Content-Type': 'application/json',
#         # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', # 设置完以后 传入的params对象就会时候用formdata传参的方式,
#         'x-auth-token': token
#     }
#     # userid = random.choice(user)
#     if i < len(user):
#         userid = user[i]
#     else:
#         m = i%len(user)
#         print(m)
#         userid = user[m]
#     print('sendtitle',title)
#     print('video_url',video_url)
#     print('userid', userid)
#     print('tagId', tagId)
#     data = {
#         "desc": title,
#         "url": str(video_url),
#         "proportion": "1920:1080",
#         "visible": 1,
#         "location": "",
#         "cityName": "",
#         "tagId": tagId,
#         "userId": userid,
#         "missionTagId": "",
#         "repeatId": repeatid
#
#     }
#     req = requests.post(insert_video_url, data=json.dumps(data), headers=headers)  # 发post请求,以json字符串参数格式
#     print(req.text)
#     if req.text == '{"code":-1,"message":"null"}':
#         time.sleep(5)
#         return None
#     return req.text

    # print(json.loads(req.text))