from selenium import webdriver
import time
# from lxml import etree
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# caps['chromeOptions'] = {'w3c':False}
# caps['showChromedriverLog'] = True
# from bs4 import BeautifulSoup
browser = webdriver.Chrome()
# browser.get('https://news.baidu.com/news?fr=mohome&$pubpathUnescape#/newslist/widthNav/info/%E8%B4%A2%E7%BB%8F')
# browser.get('https://www.toutiao.com/api/pc/list/feed?offset=0&channel_id=94349549395&max_behot_time=0&category=pc_profile_channel&disable_raw_data=true&aid=24&app_name=toutiao_web&_signature=_02B4Z6wo00101Vc5MjwAAIDANDPyVYya0TVXHRaAADaRriBv.3CsSyyy7skQkz2QoeIuicQTQWUAfVePn7eDzCTqVnDk26GKa4qddKspOibq0-cJDMxtmWDvuFxKV4nkBDbjw-BBWS7Hc94ua9')
# browser.get('https://www.toutiao.com?channel=tech&source=ch') #科技
# browser.get('https://www.toutiao.com/ch/news_hot') #热点
# browser.get('https://www.toutiao.com/ch/news_finance') #财经
# browser.get('https://www.toutiao.com/?channel=game') 游戏
# browser.get('https://www.toutiao.com/?channel=world') 国际
# browser.get('https://www.toutiao.com/?channel=food') 美食
# browser.get('https://www.toutiao.com/?channel=digital') 数码
# browser.get('https://www.toutiao.com/?channel=sports') 体育
# browser.get('https://www.toutiao.com/?channel=fashion') 时尚
# browser.get('https://www.toutiao.com/?channel=travel') 旅游
# browser.get('https://www.toutiao.com/?channel=baby') 育儿
# browser.get('https://www.toutiao.com/?channel=military&source=ch') 军事
# browser.get('https://www.toutiao.com/?channel=history&source=ch') 历史
# browser.get('https://www.toutiao.com/?channel=all&source=ch') 推荐
# browser.get('https://www.toutiao.com/?channel=regimen&source=ch') 养生
# browser.get('https://www.toutiao.com/?channel=gallery&source=ch') 图片
browser.get('https://www.toutiao.com/ch/news_entertainment') #娱乐


browser.implicitly_wait(10)
time.sleep(3)
# print(browser.page_source)
# doc = BeautifulSoup(browser.page_source, 'html.parser')
# course = doc.find('h1', class_='clp-lead__title').get_text().replace('\n','')
# print(course)

# elements = browser.find_elements_by_class_name('feed-card-article-l')
# elements = browser.find_element_by_link_text('科技').click()
# elements = browser.find_elements_by_tag_name("a")
elements = browser.find_elements_by_class_name("wtt-content")
# /html/body/div[1]/div/div[5]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/p/a
# #其他查找方法
# find_element_by_name() #通过name属性查找html元素
# find_element_by_class_name() #通过class属性中存在的值查找html元素
# find_element_by_tag_name() #通过查找标签找到元素，如传入"p", "input"等，不推荐使用
#
# #还有其他很多方法，以上均返回单个元素，element加上s则为返回多个符合条件的元素
# find_elements_by_name()

with open("4444.txt","w",encoding="utf-8") as f:
    f.write(browser.page_source)


for e in elements:
    print(e.text)
    # e.click()

# browser.close() #关闭当前窗口
# browser.quit() #关闭整个浏览器