from selenium import webdriver
import requests
from lxml import etree
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options #不显示页面
import time
opt = Options()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
#-------------------------------------
web = Chrome(options=opt)#把参数设置到浏览器
url = "https://www.toutiao.com/"

web.get(url)
text = web.page_source#得到页面element的html代码
tree = etree.HTML(text)
job_name = tree.xpath('/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div/a/p[1]/span[1]/text()')
#job = web.find_elements_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div/a/p[1]/span[1]').text
print(job_name)

# browser = webdriver.Chrome()
# browser.get('https://news.baidu.com/news#/')
