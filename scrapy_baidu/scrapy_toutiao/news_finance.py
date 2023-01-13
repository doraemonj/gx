#爬取热点新闻

from selenium import webdriver
import time,re
from scrapy_baidu.commom.news_mysql import process_item


def news_finance(times=200):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    browser = webdriver.Chrome(options=option)
    # browser = webdriver.Chrome("D:\soft\py\Google\Chrome\Application\chromedriver.exe",options=option)

    for i in range(int(20)):
        print('times', i)
        browser.get('https://www.toutiao.com/ch/news_finance') #财经
        # option = webdriver.ChromeOptions()
        # option.add_argument('headless')
        # browser = webdriver.Chrome(options=option)

        browser.implicitly_wait(10)
        time.sleep(3)
        for i in range(i):
            # browser.execute_script("window.scrollTo(0,10000)")#滑动到页面底部
            browser.execute_script("window.scrollBy(0,10000)")#滑动到页面底部
        time.sleep(3)
        href = re.findall('<div class="feed-card-article-l">(.*?)</a>', browser.page_source)



        for i in href:
            i = i.replace('<a href="', '').replace('" target="_blank" rel="noopener" class="title" aria-label=','')
            s = i.split('>')
            s[0] = s[0].split('"')
            # print(s)
            process_item(s[0][0], s[1], 18)


    browser.close() #关闭当前窗口
news_finance()