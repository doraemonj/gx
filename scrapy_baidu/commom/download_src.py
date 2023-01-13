import urllib

import requests
import uuid
pic_filePath = "D:\\pic_src\\"
video_filePath = "D:\\video_src\\"

pic_headers = {
    "User-Agent": "PostmanRuntime/7.29.2",
}

# def down_weibo(url):
#     res = requests.get(url, headers=pic_headers)
#     fileName = str(uuid.uuid4())+'.'+'png'
#     with open(pic_filePath+fileName, 'wb') as fp:
#         fp.write(res.content)
#     return fileName

def download_pic(url):
    req = requests.get(url)
    fileName = str(uuid.uuid4())+'.'+'jpg'
    # print(pic_filePath+fileName)
    with open(pic_filePath+fileName, 'wb') as f:
        f.write(req.content)
    return fileName

def download_video(url):
    print(url)
    req = requests.get(url)
    fileName = str(uuid.uuid4())+'.'+'mp4'
    print(video_filePath+fileName)
    with open(video_filePath+fileName, 'wb') as f:
        f.write(req.content)
    return fileName

import time
# def wbdownload_video(url):
#     headers = {'cookie':'XSRF-TOKEN=H9c4ulKELyVvifQHxlz8WT25; _s_tentry=weibo.com; Apache=6045480698160.99.1667105425367; SINAGLOBAL=6045480698160.99.1667105425367; ULV=1667105425383:1:1:1:6045480698160.99.1667105425367:; SSOLoginState=1667105622; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5N9UkzmMA5HaoLN-rv_31Y5JpX5KMhUgL.FoMNSoeX1hnR1h52dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS0q0ShnR1hn7; ALF=1698930234; SCF=AgU8id9Moh5-jQeIxU9ThRCFJ73ITaUyXbS1XMWab-mLcnXDhgNA0Uzw3vXQCgwb2K_3CteAFXqjmKY6Bsg5vPg.; SUB=_2A25OZhrtDeRhGeFJ7VEV-CbEwzyIHXVtEgslrDV8PUNbmtANLRHskW9Nf2ds4j_-B-6-DHLTzmK1lYoUwrjUYFDb; WBPSESS=Q51KAKiKEkoLYYTDACJFEA5n8Ai7PNMX3wVdZyZuEwbySStZFpttjfO5r4i0f8DYKqNIRBkeNmGTWS84CRRHU8YpobY77yHWdGb4slQ0GnFt5PygTc8-8QGQ3Z4Fh-KE3oJ4RU-aAwNct3n3AIeHYQ==',
#                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
#                }
#     print(url)
#     url = url.strip()
#     # url = 'https://f.video.weibocdn.com/o0/BflY0mj3lx080ooCJ9Re010412003Pze0E010.mp4?label=mp4_720p&template=720x1280.24.0&ori=0&ps=1BVp4ysnknHVZu&Expires=1667144394&ssig=mcC9YXMNjo&KID=unistore,video'
#     # url = 'http://f.video.weibocdn.com/o0/l0rurE8glx080pTih0ko010412007jXq0E010.mp4?label=mp4_720p&template=720x1280.24.0&media_id=4829246779228237&tp=8x8A3El:YTkl0eM8&us=0&ori=1&bf=4&ot=v&lp=00003MiTHW&ps=mZ6WB&uid=1N5ILX&ab=,8012-g2,8143-g0,3601-g31,8013-g0,7598-g0&Expires=1667574126&ssig=7J1DCQ4PnL&KID=unistore,video'
#     # print(url)
#     fileName = str(uuid.uuid4())+'.'+'mp4'
#
#     req = requests.get(str(url), headers)
#     # urllib.request.urlretrieve(urllib.request.urlopen(url).geturl(), fileName)
#
#     print(video_filePath+fileName)
#     # time.sleep(1)
#     with open(video_filePath+fileName, 'wb') as f:
#         f.write(req.content)
#     # time.sleep(2)
#
#     return fileName
