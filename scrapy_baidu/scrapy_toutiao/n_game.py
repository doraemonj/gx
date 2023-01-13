#爬取热点新闻

from selenium import webdriver
import time,re
from scrapy_baidu.commom.news_mysql import process_item

def news_game(times=200):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    browser = webdriver.Chrome(options=option)

    for i in range(int(200)):
        browser.get('https://www.toutiao.com/?channel=game') #游戏
        # browser.get('https://www.toutiao.com/ch/news_hot') #热点
        # browser.get('https://www.toutiao.com?channel=tech&source=ch') #科技
        # browser.get('https://www.toutiao.com/ch/news_finance') #财经
        # browser.get('https://www.toutiao.com/?channel=world') 国际
        # browser.get('https://www.toutiao.com/?channel=food') 美食
        # browser.get('https://www.toutiao.com/?channel=digital') 数码
        # browser.get('https://www.toutiao.com/?channel=sports') 体育
        # browser.get('https://www.toutiao.com/?channel=fashion') 时尚
        # browser.get('https://www.toutiao.com/?channel=baby') 育儿
        # browser.get('https://www.toutiao.com/?channel=military&source=ch') #军事
        # browser.get('https://www.toutiao.com/?channel=history&source=ch') 历史
        # browser.get('https://www.toutiao.com/?channel=all&source=ch') 推荐
        # browser.get('https://www.toutiao.com/?channel=regimen&source=ch') 养生
        # browser.get('https://www.toutiao.com/?channel=gallery&source=ch') 图片
        # browser.get('https://www.toutiao.com/ch/news_entertainment')  # 娱乐

        browser.implicitly_wait(10)
        time.sleep(3)
        for i in range(3):
            browser.execute_script("window.scrollTo(0,1000)")#滑动到页面底部
        time.sleep(0.3)
        href = re.findall('<div class="feed-card-article-l">(.*?)</a>', browser.page_source)



        for i in href:
            i = i.replace('<a href="', '').replace('" target="_blank" rel="noopener" class="title" aria-label=','')
            s = i.split('>')
            s[0] = s[0].split('"')
            # print(s)
            process_item(s[0][0], s[1], 6)


    browser.close() #关闭当前窗口

news_game()