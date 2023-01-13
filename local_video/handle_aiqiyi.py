
#上传视频
import time

from scrapy_baidu.commom.news_mysql import insert_update_video_flag
from scrapy_baidu.commom.send_detail import oss_video_pre, video_send
import os, hashlib

path2 = r"D:\handle_video"
f2 = os.listdir(path2)
count = 0
for i in f2:
    m = i.split('-')[0]
    repeatid = hashlib.md5(m.encode(encoding='UTF-8')).hexdigest()
    # print(repeatid)
    tagId = 9
    #post 视频
    # print(m)
    os_path = oss_video_pre(i,1,video_filePath=path2)
    count += 1
    #
    print('begain')
    res = video_send(m, os_path, repeatid, tagId, count)
    time.sleep(0.3)
    print('off')
    if res:
        insert_update_video_flag(m, repeatid, tagId ,os_path)
        os.remove(path2 + '\\' + i)