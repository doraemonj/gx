#爬取微博
import hashlib
import os

from selenium import webdriver
import time,re
import requests
import pprint

from scrapy_baidu.commom.download_src import down_weibo, download_video, wbdownload_video
from scrapy_baidu.commom.news_mysql import process_item, create_src_item
from scrapy_baidu.commom.save_cookies import read_cookies
from scrapy_baidu.commom.save_video import save_xigua, save_weibo
from scrapy_baidu.commom.send_detail import wboss_pic_pre, oss_video_pre, pre

pic_filePath = "D:\\pic_src\\"
video_filePath = "D:\\video_src\\"

# headers = {'cookie':'_s_tentry=weibo.com; Apache=6045480698160.99.1667105425367; SINAGLOBAL=6045480698160.99.1667105425367; ULV=1667105425383:1:1:1:6045480698160.99.1667105425367:; SUB=_2A25OWnMGDeRhGeFJ7VEV-CbEwzyIHXVtLuPOrDV8PUNbmtANLUfCkW9Nf2ds4hdiicHfv4XQoirCsSI-xTZo2Uel; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5N9UkzmMA5HaoLN-rv_31Y5JpX5KzhUgL.FoMNSoeX1hnR1h52dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS0q0ShnR1hn7; ALF=1698641621; SSOLoginState=1667105622; PC_TOKEN=64c3e4d299; WBStorage=4d96c54e|undefined',
#            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
#            }


def weiboshuaige(times=200):
    cookie = read_cookies()

    headers = {'cookie': str(cookie),
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
               }
    # for i in range(1,int(times)):
    for i in range(1,int(10)):
        # url = 'https://s.weibo.com/weibo?q=%E6%A0%A1%E8%8A%B1&Refer=SWeibo_box&page=' + str(i)
        url = 'https://s.weibo.com/weibo?q=%E5%B8%85%E5%93%A5&Refer=SWeibo_box&page=' + str(i)
        # url = 'https://s.weibo.com/weibo?q=%E7%BE%8E%E5%A5%B3&Refer=SWeibo_box&page=0&display=0&retcode=6102'


        print(url)
        response = requests.get(url=url,
                                headers=headers)
        # time.sleep(3)
        # print(response.text)

        hrefs = re.findall('<div class="card-wrap" action-type="feed_list_item" mid="(.*?)<div class="card-act">', response.text, re.S)
        print(hrefs)

        for hrefss in hrefs:
            # print(hrefss)
            hrefs_all = re.findall('node-type="feed_list_content"(.*?)</p>', hrefss, re.S)[0]
            print('hrefs_all', hrefs_all)
            html_item = ''
            find_source = re.findall('<p class="txt" node-type="feed_list_content" nick-name="(.*?)</p>', hrefss, re.S)[0]
            print('find_source', find_source)

            mid = hrefss.split('" >') #获取唯一mid
            print(mid[0])
            if find_source:
                source_name = re.findall('[\u4e00-\u9fa5]+', find_source, re.S) #获取来源名称
                # source_name = re.findall('">', find_source[0], re.S) #获取来源名称
                print('source_name', source_name[0])
            # find_s = find_source.split('<')
            # print('find_s', find_s[1])

            text_href_1 = re.findall('">(.*?)</p>', hrefs_all+'</p>', re.S)[0]
            print('111111111text_href', text_href_1)


            text_hrefs = re.sub(re.compile('<a href=' + '(.*?)</a>', re.S), '', text_href_1)
            print('text_hrefs1111111',text_hrefs)

            pictures_source = re.findall('<ul class="m(.*?)</p>', hrefss, re.S)
            if pictures_source:
                pictures_sources = pictures_source[0].split('<li><img src="')
                print('pictures_source', pictures_sources) #图片url获取
                for pics in pictures_sources:  #图片加载
                    if pics.startswith('https://wx'):
                        # print(pics)
                        pic = pics.split('"')
                        # print(pic[0]) #获取图片url
                        #下载图片到本地
                        filename = down_weibo(pic[0])
                        # print(filename)
                        #上传oss
                        os_path = wboss_pic_pre(filename, mid)
                        # print(os_path)
                        os.remove(pic_filePath + filename)
                        html_item = html_item + '<p>< img src="' + os_path +'" alt=""/></p>'
            # print('find_source', find_source)
            video_srcs = re.findall('src:(.*?)}', hrefss, re.S)  #获取视频
            # if video_src:
            for video_src in video_srcs:
                print('video_src', video_src)
                fileName = wbdownload_video('https:' + str(video_src).replace("'",''))
                time.sleep(1)
                print(fileName)
                os_path = oss_video_pre(fileName, video_src)
                print(os_path)
                html_item = html_item + '<p><video controls><source src="' + os_path + '" type="video/mp4"></video></p>'
                print(2222222222,html_item)
                # #新建数据
                # create_src_item(os_path, os_path, 'video')
                #删除本地数据
                os.remove(video_filePath + fileName)

            print('html_itemhtml_itemhtml_itemhtml_item', html_item)
            # html_item = html_item + '<br><p style="font-size:10px; color:rgb(191, 191, 191)">作品来源于%s平台，版权归作者所有。</p>' %source_name[0]
            html_item = html_item + '<br><p style="font-size:10px; color:rgb(191, 191, 191)">作品来源于微博平台，版权归作者所有。</p>'
            print('html_item111', html_item)
            repeatId = hashlib.md5()
            repeatId.update(mid[0].encode('utf-8'))
            repeatid = repeatId.hexdigest()
            print('repeatid', repeatid, repeatId)
            print(20202020, text_hrefs.strip())
            text_title = text_hrefs.strip()
            if len(text_title) > 20:
                text_title = re.findall('[\u4e00-\u9fa5]+', text_title, re.S)[0]
                print('ttttttt', text_title)
            if html_item:
                print(2222222222222222222,html_item)
                if 'img' in html_item or 'video' in html_item:
                    print(1111111111111111111111111111)
                    ret = pre(text_title, 26, html_item, repeatid, '',i) #内容上传
            # save_weibo(url, i, 26)
            save_weibo(url, 26,i,mid[0])
            time.sleep(5)

# weiboshuaige()