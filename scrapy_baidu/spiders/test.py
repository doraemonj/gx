import scrapy

from scrapy.http import Request,FormRequest

import re

import json

# from adc.items import AdcItem

from scrapy.selector import Selector

class PachSpider(scrapy.Spider):                            #定义爬虫类，必须继承scrapy.Spider

    name = 'pach'                                           #设置爬虫名称

    allowed_domains = ['news.baidu.com']                    #爬取域名

    start_urls = ['http://news.baidu.com/widget?id=civilnews&ajax=json']

    qishiurl = [                    #的到所有页面id

        'InternationalNews',

        'FinanceNews',

        'EnterNews',

        'SportNews',

        'AutoNews',

        'HouseNews',

        'InternetNews',

        'InternetPlusNews',

        'TechNews',

        'EduNews',

        'GameNews',

        'DiscoveryNews',

        'HealthNews',

        'LadyNews',

        'SocialNews',

        'MilitaryNews',

        'PicWall'

    ]

    urllieb = []

    for i in range(0,len(qishiurl)):            #构造出所有idURL

        kaishi_url = 'http://news.baidu.com/widget?id=' + qishiurl[i] + '&ajax=json'

        urllieb.append(kaishi_url)

    print(urllieb)

    def parse(self, response):                  #选项所有连接

        for j in range(0, len(self.urllieb)):

            a = '正在处理第%s个栏目:url地址是：%s' % (j, self.urllieb[j])

            yield scrapy.Request(url=self.urllieb[j], callback=self.enxt)     #每次循环到的url 添加爬虫

    def enxt(self, response):

        neir = response.body.decode("utf-8")

        pat2 = '"m_url":"(.*?)"'

        url = re.compile(pat2, re.S).findall(neir)      #通过正则获取爬取页面 的URL

        for k in range(0,len(url)):

            zf_url = url[k]

            url_zf = re.sub("\\\/", "/", zf_url)

            pduan = url_zf.find('http://')

            if pduan == 0:

                print(url_zf)
