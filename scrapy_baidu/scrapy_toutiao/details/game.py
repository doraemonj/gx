#爬取热点新闻

from selenium import webdriver
import time,re
from scrapy_baidu.commom.news_mysql import process_item

while True:
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    browser = webdriver.Chrome(options=option)

    browser.get('https://www.toutiao.com/?channel=game') #游戏


    browser.implicitly_wait(10)
    time.sleep(3)
    for i in range(3):
        browser.execute_script("window.scrollTo(0,10000)")#滑动到页面底部
    time.sleep(3)
    href = re.findall('<div class="feed-card-article-l">(.*?)</a>', browser.page_source)



    for i in href:
        i = i.replace('<a href="', '').replace('" target="_blank" rel="noopener" class="title" aria-label=','')
        s = i.split('>')
        s[0] = s[0].split('"')
        print(s[0],s[1])
        if "\"" in s[1]:
            print('s1',s[1])
            ss = s[1].replace('\"', '\\"')
            print(ss)
        if "\'" in s[1]:
            print('s1',s[1])
            ss = s[1].replace('\'', "\\'")
            print(ss)
        process_item(s[0][0], s[1], 6)


    browser.close() #关闭当前窗口