from selenium import webdriver

driver = webdriver.Chrome("C:/Users/vvv/AppData/Local/Google/Chrome/Application/chrome.exe")
def base_driver():
    # driver = webdriver.Chrome()
    # driver = webdriver.Chrome("C:/Program Files/Google/Chrome/Application/chromedriver.exe")
    driver = webdriver.Chrome("C:/Users/vvv/AppData/Local/Google/Chrome/Application/chrome.exe")
    driver.maximize_window()
    driver.get("https://news.baidu.com/news#/newslist/")
    print(driver)
    return driver


if __name__ == '__main__':
    base_driver()
import requests
from lxml import etree
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options #不显示页面
import time

# opt = Options()
# opt.add_argument('--headless')
# opt.add_argument('--disable-gpu')
# #-------------------------------------
# # web = Chrome(options=opt)#把参数设置到浏览器
# web = webdriver.Chrome("C:/Users/vvv/AppData/Local/Google/Chrome/Application/chrome.exe")
# url = "https://search.51job.com/list/130200,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%25E5%25B8%2588,2,1.html"
#
# web.get(url)
# text = web.page_source#得到页面element的html代码
# tree = etree.HTML(text)
# job_name = tree.xpath('/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div/a/p[1]/span[1]/text()')
# #job = web.find_elements_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div/a/p[1]/span[1]').text
# print(job_name)
#
# driver.get('https://cn.bing.com/')
# button_element = driver.find_element_by_id('est_cn')
# print(button_element.text)

# from selenium import webdriver
#
# from time import sleep
# #1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
# browser = webdriver.Chrome("D:/GeckoDriver/chromedriver.exe")
#
# #2.通过浏览器向服务器发送URL请求
# browser.get("https://www.baidu.com/")
#
# sleep(3)
#
# #3.刷新浏览器
# browser.refresh()
#
# #4.设置浏览器的大小
# browser.set_window_size(1400,800)
#
# #5.设置链接内容
# element=browser.find_element_by_link_text("新闻")
# element.click()
#
# element=browser.find_element_by_link_text("“下团组”时间")
# element.click()
