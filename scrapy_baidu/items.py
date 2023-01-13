# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyBaiduItem(scrapy.Item):
    # 要下载的数据
    title = scrapy.Field()
    picture = scrapy.Field()
    src = scrapy.Field()