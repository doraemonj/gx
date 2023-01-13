import scrapy
import re

from scrapy.http import Request

from scrapy_baidu.items import ScrapyBaiduItem

class BaiduNewsSpider(scrapy.Spider):
    name = 'baidu_news'
    allowed_domains = ['baidu.com']
    start_urls = ['https://news.baidu.com/widget?id=LocalNews&ajax=json']
    allid = ['LocalNews', 'civilnews', 'InternationalNews', 'EnterNews', 'SportNews', 'FinanceNews', 'TechNews',
             'MilitaryNews', 'InternetNews', 'DiscoveryNews', 'LadyNews', 'HealthNews', 'PicWall']
    allurl = []
    for url in range(0, len(allid)):
        thisid = allid[url]
        thisurl = "https://news.baidu.com/widget?id=" + thisid + "&ajax=json"
        allurl.append(thisurl)

    def parse(self, response):
        for i in range(0, len(self.allurl)):
            print("第" + str(i) + "个栏目")

            print("爬取网址：" + self.allurl[i])

            yield Request(self.allurl[i], callback=self.next)

    def next(self, response):
        print("进入next方法")
        if (response.url == 'https://news.baidu.com/widget?id=LocalNews&ajax=json'):
            data = response.body.decode("utf-8", "ignore")
            alldata = self.get_data(data, self.pattern(1))
        else:
            data = response.body.decode("utf-8", "ignore")

            alldata = self.get_data(data, self.pattern(2))
            item = NewsbaiduItem()

            item["title"] = alldata[0]

            item["link"] = alldata[1]

            yield item

    def pattern(self, choice):
        pattern = []
        if (choice == 1):
            pat1 = '"title":"(.*?)"'

            pat2 = '"url":"(.*?)"'

            pattern.append(pat1)

            pattern.append(pat2)

        elif (choice == 2):
            pat1 = '"m_title":"(.*?)"'

            pat2 = '"m_url":"(.*?)"'

            pattern.append(pat1)

            pattern.append(pat2)

        return pattern

    def get_data(self, data, pattern):
        print("调用了get_data1方法")

        pat1 = pattern[0]

        pat2 = pattern[1]

        titledata = re.compile(pat1, re.S).findall(data)
        urldata = re.compile(pat2, re.S).findall(data)
        titilall = []
        urlall = []

        for i in range(0, len(titledata)):
            thistitle = re.sub(r'(u[sS]{4})', lambda x: x.group(1).encode("utf-8").decode("unicode-escape"),

                               titledata[i])

            titilall.append(thistitle)
        for j in range(0, len(urldata)):
            thisurl = re.sub("/", "/", urldata[j])
            urlall.append(thisurl)
            alldata = []
            alldata.append(titilall)

            alldata.append(urlall)
        return self.deal_data(alldata)

    def deal_data(self, alldata):
        print("进入deal_data方法")
        if (len(alldata[0]) == len(alldata[1])):
            return alldata
        else:
            count_url = len(alldata[0]) - len(alldata[1])
        for i in range(0, count_url):

            alldata[0].pop(0)

        return alldata