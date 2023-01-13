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

    headers = {'cookie': 'XSRF-TOKEN=H9c4ulKELyVvifQHxlz8WT25; _s_tentry=weibo.com; Apache=6045480698160.99.1667105425367; SINAGLOBAL=6045480698160.99.1667105425367; ULV=1667105425383:1:1:1:6045480698160.99.1667105425367:; UPSTREAM-V-WEIBO-COM=35846f552801987f8c1e8f7cec0e2230; UOR=,,login.sina.com.cn; appkey=; WBtopGlobal_register_version=2022111722; SSOLoginState=1668693795; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5N9UkzmMA5HaoLN-rv_31Y5JpX5KMhUgL.FoMNSoeX1hnR1h52dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS0q0ShnR1hn7; ALF=1701094699; SCF=AgU8id9Moh5-jQeIxU9ThRCFJ73ITaUyXbS1XMWab-mL9_I1M4ZCPn3QGyb7oUMviIQH_c-2_ORaPih0_Ym4Lhg.; SUB=_2A25OhwH8DeRhGeFJ7VEV-CbEwzyIHXVt9XQ0rDV8PUNbmtANLRTwkW9Nf2ds4p3pZsdCXOWFdg_NXvGp_U-Yghqy; WBPSESS=Q51KAKiKEkoLYYTDACJFEA5n8Ai7PNMX3wVdZyZuEwbySStZFpttjfO5r4i0f8DYKqNIRBkeNmGTWS84CRRHU9s1lvZZq-qiZ_p6MzZ1Ot3Fv6UOc2L_2tM8TxAVarQLiGHHG6oNDPO1bkYPPBNJTQ==',
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
        html_item = ''
        hrefs = re.findall('<div class="card-wrap" action-type="feed_list_item" mid="(.*?)<div class="card-act">', response.text, re.S)
        for hrefss in hrefs:
            # contents = re.findall('<div class="content" node-type="like">(.*?)</div><div>',  response.text, re.S)
            mid = hrefss.split('" >')[0] #获取唯一mid
            print('mid88888',mid)
            # print(contents)
            # content1 = re.findall('<p class="txt" node-type="feed_list_content" nick-name="(.*?)</p>', response.text, re.S)
            content2 = re.findall('<p class="txt" node-type="feed_list_content_full" nick-name="(.*?)</p>', hrefss, re.S)
            # # print(1111111111,content1)
            # print(222222222,content2)
            # for con in content1:
            #     print(333333333,con)
            img_hrefs_all = re.findall('<div class="media media-piclist" node-type="(.*?)</ul>', hrefss, re.S)
            # print('img_hrefs_all', img_hrefs_all)

            if content2:
                print(444444,content2)
                cons = re.findall('style="display: none">(.*?)收起<i class="wbicon">d</i></a>',
                                  content2[0], re.S)
                print(5555,cons)
                if cons:
                    lines = cons[0]
                    # print(11111111111,lines)
                    line = lines.replace('<a href="javascript:void(0);" action-type="fl_fold">','')
                    # print(666666666666,line)
                    deal_lines = re.sub(re.compile('<img src="(.*?)/>', re.S), '', line)
                    deal_line1 = re.sub(re.compile('<a href="(.*?)>', re.S), '', deal_lines)
                    deal_line = re.sub(re.compile('<i class=(.*?)</i>', re.S), '', deal_line1)
                    if '</a>' in deal_line:
                        deal_line = deal_line.replace('</a>','')
                    if '<br/>' in deal_line:
                        deal_line = deal_line.replace('<br/>','')
                    html_item = '<p>' + deal_line + '</p>'
                    print(7777777,deal_line)

            #
                if deal_line:
                    text_title1 = ''
                    text_final = ''
                    text_title = re.findall('[\u4e00-\u9fa5]+', deal_line, re.S)[0]
                    print(text_title)
                    if '】' in deal_line:
                        text_title1 = deal_line.split('】')[0]
                        text_final = text_title1 + '】'
                    else:
                        text_final = text_title
                    print('text_title', text_title)
                    print('text_title1', text_title1)
                    print('text_final',text_final)
                    for imgs in img_hrefs_all:
                        pictures_sources = re.findall('<img src="(.*?)"', imgs, re.S)
                        print('pictures_sources',pictures_sources)
                        # 下载图片到本地
                        for pic in pictures_sources:
                            filename = down_weibo(pic)
                            print(filename)
                            #上传oss
                            os_path = wboss_pic_pre(filename, mid)
                            print(os_path)
                            os.remove(pic_filePath + filename)
                            html_item = html_item + '<p><img src="' + os_path +'" alt=""/></p>'
                    print('html_itemhtml_item',html_item)
                    repeatId = hashlib.md5()
                    repeatId.update(mid.encode('utf-8'))
                    repeatid = repeatId.hexdigest()
                    if html_item:
                        if '（来源：中国雄安官网）' in html_item:
                            html_item = html_item.replace('（来源：中国雄安官网）','')
                        html_item = html_item + '<br><p style="font-size:10px; color:rgb(191, 191, 191)">作品来源于微博平台，版权归作者所有。</p>'
                        ret = pre_luntan(text_final, 11, html_item, repeatid, '',max_count) #内容上传
                        max_count += 1
                    if max_count == 100:
                        print('break')
                        sys.exit(0)
                    save_weibo(url, 11,i,mid[0])
                # time.sleep(0.1)
                # break
        #     if html_item:
        #         print(2222222222222222222,html_item)
        #         # if 'img' in html_item or 'video' in html_item:
        #         #     # print(1111111111111111111111111111)
        #         #     print('html_item111111111111',html_item)
        #         #     print('html_item22222222',text_title)
        #         #
        #         #     if text_title2:
        #         #         if '<br/>' in text_title2:
        #         #             text_title2 = text_title2.replace('<br/>', '')
        #         #         # if len(text_title2) < 30:
        #         #         html_itemt = '<p><br>' + text_title2 + '<br></p>'
        #         #
        #         #         html_item = html_itemt + html_item
        #         #         print('html_itemhtml_itemhtml_item1',html_item)
        #         #         ret = pre_luntan('', 11, html_item, repeatid, '',max_count) #内容上传
        #         #         max_count += 1
        #         #     elif text_title:
        #         #         if '<br/>' in text_title:
        #         #             text_title = text_title.replace('<br/>', '')
        #         #         # if len(text_title) < 30:
        #         #         html_itemt = '<p><br>' + text_title + '<br></p>'
        #         #
        #         #         html_item = html_itemt + html_item
        #         #         print('html_itemhtml_itemhtml_item2',html_item)
        #         #         ret = pre_luntan('', 11, html_item, repeatid, '',max_count) #内容上传
        #         #         max_count += 1
        #         #     print('max_count',max_count)
        #         #     if max_count == 5:
        #         #         print('break')
        #         #         sys.exit(0)
        #     # save_weibo(url, 11,i,mid[0])
        #     time.sleep(5)

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