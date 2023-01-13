from scrapy_baidu.commom.news_mysql import save_car_item

max_behot_time=1667057970
 
import time ,requests

# headers = {'cookie':'_s_tentry=weibo.com; Apache=6045480698160.99.1667105425367; SINAGLOBAL=6045480698160.99.1667105425367; ULV=1667105425383:1:1:1:6045480698160.99.1667105425367:; SSOLoginState=1667105622; PC_TOKEN=2437bdf612; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5N9UkzmMA5HaoLN-rv_31Y5JpX5KMhUgL.FoMNSoeX1hnR1h52dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS0q0ShnR1hn7; ALF=1698930234; SCF=AgU8id9Moh5-jQeIxU9ThRCFJ73ITaUyXbS1XMWab-mLcnXDhgNA0Uzw3vXQCgwb2K_3CteAFXqjmKY6Bsg5vPg.; SUB=_2A25OZhrtDeRhGeFJ7VEV-CbEwzyIHXVtEgslrDV8PUNbmtANLRHskW9Nf2ds4j_-B-6-DHLTzmK1lYoUwrjUYFDb',
#            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
#            }
# url = 'https://www.dongchedi.com/motor/stream_entrance/get_feed_pc/v47/?tt_from=enter_auto&category=motor_car&motor_feed_extra_params=%7B%22new_feed%22%3Atrue%2C%22feed_type%22%3A0%7D&impression_info=%7B%22page_id%22%3A%22page_car_series%22%2C%22sub_tab%22%3A%22motor_car%22%2C%22product_name%22%3A%22web%22%7D&aid=1839&refer=1&channel=web&device_platform=web&web_id=7154758952428570119&motor_feed_extra_params=%7B%22new_feed%22%3Atrue%2C%22feed_type%22%3A0%7D&source=pc'
def dongchedi(time=200):
    for i in range(int(time)):
        url = 'https://www.dongchedi.com/motor/stream_entrance/get_feed_pc/v47/?tt_from=enter_auto&category=motor_car&motor_feed_extra_params=%7B%22new_feed%22%3Atrue%2C%22feed_type%22%3A0%7D&impression_info=%7B%22page_id%22%3A%22page_car_series%22%2C%22sub_tab%22%3A%22motor_car%22%2C%22product_name%22%3A%22web%22%7D&aid=1839&refer=1&channel=web&device_platform=web&web_id=7154758952428570119&motor_feed_extra_params=%7B%22new_feed%22%3Atrue%2C%22feed_type%22%3A0%7D&source=pc&max_behot_time=' + str(time.time())
        # print(time.time()-max_behot_time)

        # response = requests.get(url=url, headers=headers)
        response = requests.get(url=url)
        print(response.json())
        response = response.json().get('data')
        for article_urls in response:
            article_url = article_urls.get('info').get('article_url')
            title = article_urls.get('info').get('title')
            save_car_item(article_url,title, 24, str(time.time()))