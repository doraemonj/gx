import threading
from time import sleep,ctime

from scrapy_baidu.detail_all.car_detail import download_car_detail
from scrapy_baidu.detail_all.fashion_detail import download_fashion_detail
from scrapy_baidu.detail_all.finance_detail import download_finance_detail
from scrapy_baidu.detail_all.food_detail import download_food_detail
from scrapy_baidu.detail_all.game_detail import download_game_detail
from scrapy_baidu.detail_all.hot_detail import download_hot_detail
from scrapy_baidu.detail_all.military_detail import download_military_detail
from scrapy_baidu.detail_all.tech_detail import download_tech_detail
from scrapy_baidu.detail_all.tiyu_detail import download_tiyu_detail
from scrapy_baidu.detail_all.travel_detail import download_travel_detail
from scrapy_baidu.detail_all.word_detail import download_word_detail
from scrapy_baidu.detail_all.yangsheng_detail import download_yangsheng_detail
from scrapy_baidu.detail_all.yule_detail import download_yule_detail
from scrapy_baidu.scrapy_toutiao.fashion import news_fashion


loops_detail = [download_car_detail,download_fashion_detail,download_finance_detail,download_food_detail,download_game_detail,
         download_hot_detail,download_military_detail,download_tech_detail,download_tiyu_detail,download_travel_detail,
         download_word_detail,download_yangsheng_detail,download_yule_detail]



# def loop(nloop,nsec):
#     print('start loop',nloop,'at:',ctime())
#     sleep(nsec)
#     print('loop',nloop,'done at:',ctime())

def main():
    print('starting at:',ctime())
    threads = []

    nloops = list(range(len(loops_detail)))
    for i in nloops:
        t = threading.Thread(target=i)
        threads.append(t)
    for i in threads:
        i.start()



if __name__ == '__main__':
    main()