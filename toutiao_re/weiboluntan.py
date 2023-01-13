#爬取微博
import hashlib
import os
import sys

from selenium import webdriver
import time,re
import requests
import pprint

from scrapy_baidu.commom.download_src import down_weibo, download_video, wbdownload_video
from scrapy_baidu.commom.news_mysql import process_item, create_src_item
# from scrapy_baidu.commom.save_cookies import read_cookies
from scrapy_baidu.commom.save_video import save_xigua, save_weibo
from scrapy_baidu.commom.send_detail import wboss_pic_pre, oss_video_pre, pre_luntan

pic_filePath = "D:\\pic_src\\"
video_filePath = "D:\\video_src\\"

# headers = {'cookie':'_s_tentry=weibo.com; Apache=6045480698160.99.1667105425367; SINAGLOBAL=6045480698160.99.1667105425367; ULV=1667105425383:1:1:1:6045480698160.99.1667105425367:; SUB=_2A25OWnMGDeRhGeFJ7VEV-CbEwzyIHXVtLuPOrDV8PUNbmtANLUfCkW9Nf2ds4hdiicHfv4XQoirCsSI-xTZo2Uel; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5N9UkzmMA5HaoLN-rv_31Y5JpX5KzhUgL.FoMNSoeX1hnR1h52dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS0q0ShnR1hn7; ALF=1698641621; SSOLoginState=1667105622; PC_TOKEN=64c3e4d299; WBStorage=4d96c54e|undefined',
#            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
#            }

def weiboluntan(times=100):
    # print('times',times)
    # cookie = read_cookies()
    max_count = 0

    headers = {'cookie': '_s_tentry=weibo.com; Apache=6045480698160.99.1667105425367; SINAGLOBAL=6045480698160.99.1667105425367; ULV=1667105425383:1:1:1:6045480698160.99.1667105425367:; SSOLoginState=1667105622; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5N9UkzmMA5HaoLN-rv_31Y5JpX5KMhUgL.FoMNSoeX1hnR1h52dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS0q0ShnR1hn7; ALF=1700225720; SCF=AgU8id9Moh5-jQeIxU9ThRCFJ73ITaUyXbS1XMWab-mLkBo5N3FICt_6HmOTEn__CL5khSxri8w5dzJYVZJH2yU.; SUB=_2A25Ocl9pDeRhGeFJ7VEV-CbEwzyIHXVtBjehrDV8PUNbmtANLUelkW9Nf2ds4j0V8KdLI2ccTJrFpzsZVwHYWFPT; UOR=,,login.sina.com.cn',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
               }

    for i in range(1,int(20)):
        # url = 'https://s.weibo.com/weibo?q=%E6%A0%A1%E8%8A%B1&Refer=SWeibo_box&page=' + str(i)
        # url = 'https://s.weibo.com/weibo?q=%E7%BE%8E%E5%A5%B3&Refer=SWeibo_box&page=' + str(i)
        # url = 'https://s.weibo.com/weibo?q=%E8%AE%BA%E5%9D%9B&Refer=SWeibo_box&page=' + str(i)
        url = 'https://s.weibo.com/weibo/%E8%AE%BA%E5%9D%9B&page=' + str(i)
        # url = 'https://s.weibo.com/weibo?q=%E7%BE%8E%E5%A5%B3&Refer=SWeibo_box&page=0&display=0&retcode=6102'


        print(url)
        response = requests.get(url=url,
                                headers=headers)
        # time.sleep(3)
        # print(response.text)

        hrefs = re.findall('<div class="card-wrap" action-type="feed_list_item" mid="(.*?)<div class="card-act">', response.text, re.S)
        # print(hrefs)

        for hrefss in hrefs:
            # print(hrefss)
            hrefs_all = re.findall('node-type="feed_list_content"(.*?)</p>', hrefss, re.S)[0]
            print('hrefs_all', hrefs_all)
            img_hrefs_all = re.findall('<li action-data="uid=(.*?)"></i>', hrefss, re.S)
            print('img_hrefs_all', img_hrefs_all)
            html_item = ''
            find_source = re.findall('<p class="txt" node-type="feed_list_content" nick-name="(.*?)</p>', hrefss, re.S)[0]
            # print('find_source', find_source)

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


            for imgs in img_hrefs_all:
                pictures_sources = re.findall('<img src="(.*?)"', imgs, re.S)
                print('pictures_sources',pictures_sources)
                # 下载图片到本地
                if pictures_sources:
                    filename = down_weibo(pictures_sources[0])
                    print(filename)
                    #上传oss
                    os_path = wboss_pic_pre(filename, mid)
                    print(os_path)
                    os.remove(pic_filePath + filename)
                    html_item = html_item + '<p><img src="' + os_path +'" alt=""/></p>'

            video_srcs = re.findall('src:(.*?)}', hrefss, re.S)  #获取视频


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


            print('html_item', html_item)
            # html_item = html_item + '<br><p style="font-size:10px; color:rgb(191, 191, 191)">作品来源于%s平台，版权归作者所有。</p>' %source_name[0]
            # html_item = html_item + '<br><p style="font-size:10px; color:rgb(191, 191, 191)">作品来源于微博平台，版权归作者所有。</p>'
            html_item = html_item
            print('html_item111', html_item)
            repeatId = hashlib.md5()
            repeatId.update(mid[0].encode('utf-8'))
            repeatid = repeatId.hexdigest()
            # print('repeatid', repeatid, repeatId)
            # print(20202020, text_hrefs.strip())
            text_title = text_hrefs.strip()
            print('text_titletext_titletext_title', text_title)
            text_title2 = text_title.split('<br/>')[0]
            print('text_title2',text_title2)
            if 'img' in text_title2:
                img_src = re.findall('<img src="(.*?)/>', text_title2, re.S)
                for img in img_src:
                    text_title2 = text_title2.replace('<img src="'+img+'/>','')
                    print('img_src',img_src)
            print('text_title3',text_title2)

            text_title1 = re.findall('[\u4e00-\u9fa5]+', text_title, re.S)
            if len(text_title) > 60 or 'img' in text_title:
                text_title = re.findall('[\u4e00-\u9fa5]+', text_title, re.S)[0]
                print('ttttttt', text_title)
            print('ttttttt1111111', text_title1)
            if html_item:
                print(2222222222222222222,html_item)
                if 'img' in html_item or 'video' in html_item:
                    # print(1111111111111111111111111111)
                    print('html_item111111111111',html_item)
                    print('html_item22222222',text_title)

                    if text_title2:
                        if '<br/>' in text_title2:
                            text_title2 = text_title2.replace('<br/>', '')
                        # if len(text_title2) < 30:
                        html_itemt = '<p><br>' + text_title2 + '<br></p>'

                        html_item = html_itemt + html_item
                        print('html_itemhtml_itemhtml_item1',html_item)
                        ret = pre_luntan('', 11, html_item, repeatid, '',max_count) #内容上传
                        max_count += 1
                    elif text_title:
                        if '<br/>' in text_title:
                            text_title = text_title.replace('<br/>', '')
                        # if len(text_title) < 30:
                        html_itemt = '<p><br>' + text_title + '<br></p>'

                        html_item = html_itemt + html_item
                        print('html_itemhtml_itemhtml_item2',html_item)
                        ret = pre_luntan('', 11, html_item, repeatid, '',max_count) #内容上传
                        max_count += 1
                    print('max_count',max_count)
                    if max_count == 5:
                        print('break')
                        sys.exit(0)
            save_weibo(url, 11,i,mid[0])
            time.sleep(5)

weiboluntan(2)
# img_hrefs_all=['1708942053&pic_id=001RExTvly1h7yzclg5eqj61xi134x6p02" action-type="fl_pics" suda-data="key=tblog_search_weibo&value=weibo_ss_1_pic" style="width: 296px;"><img src="https://wx4.sinaimg.cn/orj360/001RExTvly1h7yzclg5eqj61xi134x6p02.jpg" style="position: relative;width: 296px;top: -0px;left: -15px;display: block"><i class="picture-cover" style="width: 296px;left: -15px;']
#
# print('len',len(img_hrefs_all))
# img_src = ''
# for imgs in img_hrefs_all:
#
#     # ims = imgs.split('<img src="')
#     ims = re.findall('<img src="(.*?)"', imgs, re.S)
#     # ims = re.compile('<img src="(.*?)">', re.S)
#     print(ims[0])