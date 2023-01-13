import hashlib, os

from selenium import webdriver
import time,re,json,base64

from scrapy_baidu.commom.download_src import download_video
from scrapy_baidu.commom.news_mysql import process_item, update_video_flag
from scrapy_baidu.commom.save_video import save_xigua, read_item, save_tengxun
import requests

from scrapy_baidu.commom.send_detail import oss_video_pre, video_send

option = webdriver.ChromeOptions()
# option.add_argument('headless')
browser = webdriver.Chrome(options=option)
for i in range(1,28):
    url = 'https://v.qq.com/x/search/?searchSession=tabid=%E5%85%A8%E9%83%A8%E9%A2%91%E9%81%93|0,%E7%94%B5%E8%A7%86%E5%89%A7|2,%E7%94%B5%E5%BD%B1|1,%E7%BB%BC%E8%89%BA|3,%E5%8A%A8%E6%BC%AB|4,%E6%96%B0%E9%97%BB|11,%E7%BA%AA%E5%BD%95%E7%89%87|6,%E5%A8%B1%E4%B9%90|12,%E6%B1%BD%E8%BD%A6|21,%E4%BD%93%E8%82%B2|14,%E9%9F%B3%E4%B9%90|5,%E6%B8%B8%E6%88%8F|17,%E5%8E%9F%E5%88%9B|8,%E8%B4%A2%E7%BB%8F|13,%E6%95%99%E8%82%B2|15,%E6%AF%8D%E5%A9%B4|20,%E5%B0%91%E5%84%BF|106,%E5%85%B6%E5%AE%83|7&firstTabid=%E5%85%A8%E9%83%A8|0,%E7%94%A8%E6%88%B7|103&q=%E6%AC%A7%E7%BE%8E&preQid=Pjwpq-WpV5rD52KYj_w6mnHwNPeaDXM3haaPmNlGKroFpMbaoKmCPA&queryFrom=3&cur='+ str(i)+'&isNeedQc=true&_=1668914592698'
    browser.get(url) #腾讯
    browser.implicitly_wait(10)

    video_href = re.findall('<div class="result_item result_item_h" data-suggest="(.*?)</div>', browser.page_source, re.S)
    # print(video_href)
    for v_detail in video_href:
        # print(1111111111,v_detail)
        video_hrefs = re.findall('<h2 class="result_title">(.*?)</h2>', v_detail, re.S)[0]
        vide_url = re.findall('<a href="(.*?)"', video_hrefs, re.S)[0]
        print(22222222,vide_url)
        title_txt = re.findall('title_txt=(.*?)"', video_hrefs, re.S)[0]
        video_time = re.findall('<span class="figure_info">(.*?)</span>', v_detail, re.S)[0]
        print(33333333,title_txt)
        print(44444,video_time)


        title =title_txt
        # print(title)
        href = vide_url
        # print(href)
        target = ''
        # print(target)
        save_tengxun(title, href, target, video_time, type=9)

# source_ele = browser.find_element_by_class_name('search_container').text
# print(source_ele)
# print(browser.page_source)
