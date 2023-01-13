#爬取热点新闻

from selenium import webdriver
import time,re
from scrapy_baidu.commom.news_mysql import process_item

browser = webdriver.Chrome()

browser.get('https://www.toutiao.com/ch/news_hot') #热点


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
    # print(s)
    process_item(s[0][0], s[1], 1)


browser.close() #关闭当前窗口