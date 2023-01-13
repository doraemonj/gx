from selenium import webdriver
import time,re
from lxml import etree

browser = webdriver.Chrome()

browser.get('https://www.toutiao.com/ch/news_hot') #热点


browser.implicitly_wait(10)
time.sleep(3)
elements = browser.find_elements_by_class_name('feed-card-article-l')
# print(elements[0].get_attribute("href"))
# print(elements[1].get_attribute("href"))
# elements = browser.find_element_by_xpath('//*[@id="root"]/div/div[5]/div[1]/div/div/div/div[2]/div[1]/div/div/a')
# print(elements.get_attribute("href"))
# elements = browser.find_element_by_xpath('//*[@id="root"]/div/div[5]/div[1]/div/div/div/div[2]/div[2]/div/div/a')
# print(elements.get_attribute("href"))
# elements = browser.find_elements_by_xpath('//*[@id="root"]/div/div[5]/div[1]/div/div/div/div[2]/*/a')
# elements = browser.find_elements_by_xpath('//a')
# print(elements.get_attribute("href"))
# print(browser.page_source)
# for i in range(3): #滚动条
#     js = "var q = document.documentElement.scrollTOP="+str(i*500)
#     browser.execute_script(js)

browser.execute_script("window.scrollTo(0,10000)")#滑动到页面底部

# print(browser.page_source)


# with open("news_hot.txt","w",encoding="utf-8") as f:
#     f.write(browser.page_source)
#
#

# length = len(browser.find_elements_by_tag_name("a")
# len_ele = len(elements)
#
# for i in range(0,len_ele):
#     links = elements
#     link = links[i]
#     # if not ("_blank" in link.get_attribute("target") or "http" in link.get_attribute("href")):
#     link.click()
#     browser.back()

# for e in elements:
#     print(e.text)
# print(elements)
# for url in elements:
#     print(url.get_attribute("href"))
# for e in elements:
#     try:
#         click_ele = e.click()
#         handles = browser.window_handles
#         print(handles,browser.current_window_handle,browser.current_url)
#         for handle in handles:
#             if handle != browser.current_window_handle:
#                 # browser.close()
#                 print(e.text)
#                 time.sleep(5)
#                 # handle = browser.window_handles[0]
#                 browser.switch_to.window(handle)
#                 time.sleep(1)
#                 print('当前浏览器地址为：.{}'.format(browser.current_url))
#                 browser.switch_to.window(browser.current_window_handle)
#                 # # browser.switch_to.window(browser.window_handles[2])
#                 # time.sleep(1)
#
#
#     except Exception as e:
#             print(e)

# page = browser.page_source
# doc = etree.HTML(str(page))
# contents = doc.xpath('//div[@class="ttp-feed-module"]')
# print(contents)
# for i in contents:
#     print(i)
#     title = i.xpath('/div[2]')
ale = []
for e in elements:
    # print(e.text)
    ale.append(e.text)
    # print(e.get_attribute("href"))

# for text in ale:
#     browser.find_element_by_link_text(text)
# p_href = '<div class="feed-card-article-l">(.*?)</div>'
p_href = r'(?:<div class="feed-card-article-l">)(.*)(?:</div>)'
# p_href = r'<div class="feed-card-article-l"><a href="(.*?)</a>'
href = re.findall(p_href, browser.page_source)
href = re.findall('<div class="feed-card-article-l">(.*?)</a>', browser.page_source)
print(href)

# browser.close() #关闭当前窗口

for i in href:
    print(i)
    with open("news_hot.txt","w",encoding="utf-8") as f:
        f.write(i)
