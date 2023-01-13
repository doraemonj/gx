# #爬取微博
# import hashlib
# import os
#
# from selenium import webdriver
# import time,re
# import requests
# import pprint
#
# from scrapy_baidu.commom.download_src import down_weibo, download_video, wbdownload_video
# from scrapy_baidu.commom.news_mysql import process_item, create_src_item
# from scrapy_baidu.commom.save_video import save_xigua, save_weibo
# from scrapy_baidu.commom.send_detail import wboss_pic_pre, oss_video_pre, pre
#
# pic_filePath = "D:\\pic_src\\"
# video_filePath = "D:\\video_src\\"
#
# # headers = {'cookie':'_s_tentry=weibo.com; Apache=6045480698160.99.1667105425367; SINAGLOBAL=6045480698160.99.1667105425367; ULV=1667105425383:1:1:1:6045480698160.99.1667105425367:; SUB=_2A25OWnMGDeRhGeFJ7VEV-CbEwzyIHXVtLuPOrDV8PUNbmtANLUfCkW9Nf2ds4hdiicHfv4XQoirCsSI-xTZo2Uel; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5N9UkzmMA5HaoLN-rv_31Y5JpX5KzhUgL.FoMNSoeX1hnR1h52dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS0q0ShnR1hn7; ALF=1698641621; SSOLoginState=1667105622; PC_TOKEN=64c3e4d299; WBStorage=4d96c54e|undefined',
# #            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
# #            }
#
# headers = {'cookie':'XSRF-TOKEN=H9c4ulKELyVvifQHxlz8WT25; _s_tentry=weibo.com; Apache=6045480698160.99.1667105425367; SINAGLOBAL=6045480698160.99.1667105425367; ULV=1667105425383:1:1:1:6045480698160.99.1667105425367:; SSOLoginState=1667105622; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5N9UkzmMA5HaoLN-rv_31Y5JpX5KMhUgL.FoMNSoeX1hnR1h52dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS0q0ShnR1hn7; ALF=1698930234; SCF=AgU8id9Moh5-jQeIxU9ThRCFJ73ITaUyXbS1XMWab-mLcnXDhgNA0Uzw3vXQCgwb2K_3CteAFXqjmKY6Bsg5vPg.; SUB=_2A25OZhrtDeRhGeFJ7VEV-CbEwzyIHXVtEgslrDV8PUNbmtANLRHskW9Nf2ds4j_-B-6-DHLTzmK1lYoUwrjUYFDb; WBPSESS=Q51KAKiKEkoLYYTDACJFEA5n8Ai7PNMX3wVdZyZuEwbySStZFpttjfO5r4i0f8DYKqNIRBkeNmGTWS84CRRHU8YpobY77yHWdGb4slQ0GnFt5PygTc8-8QGQ3Z4Fh-KE3oJ4RU-aAwNct3n3AIeHYQ==',
#            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
#            }
# # https://weibo.com/ajax/feed/hottimeline?refresh=1&group_id=1028031588&containerid=102803_ctg1_1588_-_ctg1_1588&extparam=discover%7Cnew_feed&max_id=0&count=10
# # https://weibo.com/ajax/feed/hottimeline?refresh=2&group_id=1028035488&containerid=102803_ctg1_5488_-_ctg1_5488&extparam=discover%7Cnew_feed&max_id=1&count=10
#
#
# for i in range(100):
#     max_id = i
#     # url = 'https://weibo.com/ajax/feed/hottimeline?refresh=2&group_id=1028035488&containerid=102803_ctg1_5488_-_ctg1_5488&extparam=discover%7Cnew_feed&max_id='+str(i)+'&count=10'
#     # url = 'https://s.weibo.com/weibo?q=%E7%BE%8E%E5%A5%B3&Refer=SWeibo_box&page=0&display=0&retcode=6102'
#     # url = 'https://weibo.com/ajax/feed/hottimeline?refresh=1&group_id=1028032388&containerid=102803_ctg1_2388_-_ctg1_2388&extparam=discover|new_feed&max_id='+str(i)+'&count=10'
#     url = 'https://weibo.com/ajax/feed/groupstimeline?list_id=110057763488880&refresh=4&fast_refresh=1&count=25'
#     url = 'https://weibo.com/ajax/feed/groupstimeline?list_id=110057763488880&refresh=4&fast_refresh=1&count=25'
#     # print(url)
#     response = requests.get(url=url,
#                         headers=headers)
#     # time.sleep(3)
#     # print(response.json())
#
#     response = response.json()
#     statuses = response.get('statuses')
#
#
#     for statuse in statuses:
#         html_item = ''
#         # print('statuse',statuse)
#         mid = statuse.get('mid')
#         print(mid)
#         text_raw = statuse.get('text_raw')
#         # print(1111111111,text_raw)
#         if 'http' in text_raw:
#             text_raw = text_raw.split('http')[0]
#         print(22222222222, text_raw)
#         title = text_raw
#         pic_ids = statuse.get('pic_ids')
#         pic_infos = statuse.get('pic_infos')
#         pic_num = statuse.get('pic_num')
#         page_info = statuse.get('page_info')
#         if pic_num:
#             for i in range(0, pic_num):
#                 pic_info = pic_infos.get(pic_ids[i])
#                 # print(pic_info)
#                 original_url = pic_info.get('original').get('url')
#                 print(original_url)
#                 filename = down_weibo(original_url)
#                 print(pic_ids[i])
#                 os_path = wboss_pic_pre(filename, pic_ids[i])
#                 os.remove(pic_filePath + filename)
#                 html_item = html_item + '<p><img src="' + os_path +'" alt=""/></p>'
#                 # html_item = html_item + '<p>< img src="' + original_url +'" alt=""/></p>'
#         if page_info:
#             media_info = page_info.get('media_info')
#             print('media_info',media_info)
#             if media_info:
#                 media_id = media_info.get('media_id')
#                 playback_list = media_info.get('playback_list')
#                 if playback_list:
#                     play_info = playback_list[0].get('play_info')
#                     if play_info:
#                         play_url = play_info.get('url')
#                 # print('media_id',media_id)
#                 mp4_720p_mp4 = media_info.get('mp4_720p_mp4')
#                 # print('mp4_720p_mp4',mp4_720p_mp4)
#                 # if mp4_720p_mp4:
#                 #     mp4_720p_mp4 = mp4_720p_mp4.strip()
#                 #     print(mp4_720p_mp4)
#                 #     fileName = wbdownload_video(mp4_720p_mp4)
#                 #     time.sleep(1)
#                 #     # print(fileName)
#                 #     os_path = oss_video_pre(fileName, mp4_720p_mp4)
#                 #     print(os_path)
#                 if play_url:
#                     play_url = play_url.strip()
#                     print(play_url)
#                     fileName = wbdownload_video(play_url)
#                     time.sleep(1)
#                     # print(fileName)
#                     os_path = oss_video_pre(fileName, play_url)
#                     print(os_path)
#
#                     html_item = html_item + '<p><video controls><source src="' + os_path + '" type="video/mp4"></video></p>'
#
#                     os.remove(video_filePath + fileName)
#
#             # html_item = html_item + '<p><video controls><source src="' + mp4_720p_mp4 + '" type="video/mp4"></video></p>'
#         repeatId = hashlib.md5()
#         repeatId.update(mid.encode('utf-8'))
#         repeatid = repeatId.hexdigest()
#         # print('repeatid', repeatid, repeatId)
#         if html_item:
#             html_item = html_item + '<br><p style="font-size:10px; color:rgb(191, 191, 191)">作品来源于微博平台，版权归作者所有。</p>'
#             ret = pre(title, 10, html_item, repeatid, '') #内容上传
#         save_weibo(url, 10,mid,max_id)
#         print(html_item)