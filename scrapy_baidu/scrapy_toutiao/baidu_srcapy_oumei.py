#爬取好看视频

from selenium import webdriver
import time,re
import requests
import pprint
from scrapy_baidu.commom.news_mysql import process_item
from scrapy_baidu.commom.save_video import save_xigua

url = 'https://haokan.baidu.com/web/search/api?pn=1&rn=10&type=video&query=%E6%AC%A7%E7%BE%8E%E7%94%B5%E5%BD%B1'
# p = {
#     'pn': 1,
#     'rn': 10,
#     'type': 'video',
#     'query': '%E6%AC%A7%E7%BE%8E%E7%94%B5%E5%BD%B1'
# }

heads = {
    'cookie': 'BIDUPSID=8FC47947011F57D9176BCA81E2579A7E; PSTM=1665110861; BAIDUID=8FC47947011F57D9B1BD66F5BDE28225:FG=1; H_WISE_SIDS=110085_204427_204916_209568_210321_212295_212740_212868_213039_213360_214796_215730_216845_216941_217168_218549_219245_219565_219942_219946_220017_220663_221479_221795_221874_222299_222425_222625_223064_223211_223683_223906_224046_224077_224086_224159_224456_224633_225564_225593_225764_225846_225860_226006_226102_226270_226550_226628_226718_226815_226965_227063_227187_227515_227528_227747_227865_227869_227932_227941_227973_228138_228369_228380_228424_228507_228774_228807_228833_228978_229029_229033_229062_229125_229154_229286_229411_229525_229685_229750_229914_229918_229938_229967_230020_230040_230089_230237_230240_230244_230249_230305_230437_230468_230544_230686_230707_230861_230911_230930; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDSFRCVID=mduOJeC62rvsNQ7jSlVTU9Ok38g4MbJTH6f3Y9q_pPV_qG9fDYcCEG0PaM8g0Kub1DMtogKKL2OTHmuF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tJIJ_ID2JCD3enTmbt__-P4DeUcb-xRZ5mAqotoK-hrGMncbhhjx3jFgMN-OK53uKeQnaIQDtMIBqf7x0hjrKfb-b4Ok5MJ43bRT3lCy5KJvfJ_lQMcMhP-UyPkHWh37a6TlMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMonLafJOKHIClD5uBDxa; BDUSS=dtV000TVE1d210Z1VMZnduZEJHUm1HM24tdjFETWNWVFlTYnNTTDFheGphWU5qSVFBQUFBJCQAAAAAAAAAAAEAAAA5mBxx7bntue257bntue25MQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGPcW2Nj3FtjNX; BDUSS_BFESS=dtV000TVE1d210Z1VMZnduZEJHUm1HM24tdjFETWNWVFlTYnNTTDFheGphWU5qSVFBQUFBJCQAAAAAAAAAAAEAAAA5mBxx7bntue257bntue25MQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGPcW2Nj3FtjNX; H_PS_PSSID=26350; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1666330671,1667054298; hkpcSearch=%u6B27%u7F8E%u7535%u5F71%24%24%24%u6B27%u7F8E; PC_TAB_LOG=video_details_page; COMMON_LID=48664518cf6f29d4bc6ef0499309effd; ab_sr=1.0.1_NmY3YjA2MDViZTIzZjIyMmY3MGM1NWZkZjdiZjA3NDU0NWEyMjY2OTY5MmE0MDgzNTE1Mjg1M2JmNDI1M2QwMGY4YjE1MzE5ZmJiNWU4MDYwODJmMzBjZjk0OGI4OWE4YjE5ODIxMmQyNmEwMjEwOTVlOGZkMzA3YjNkZjJkNzE2OTQ1ZWNiNWZlZTBmNmVjYzkzNGUxZThhOWIwMDlkZg==; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1667056994; reptileData=%7B%22data%22%3A%22a4925e90b6e2dc93225045e44f90e728521c8d354952f17d4325d19acb9b59b7efdc9004ed0ab0201593cdb7eea807c27d662dd79cc272dc12faf2ad7e75d834db50303a31995e3cb2b97d683e762e62926f7c54d430687dd30ffb64288ffa95%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%22afe14bb0%22%7D; delPer=0; PSINO=5; BAIDUID_BFESS=8FC47947011F57D9B1BD66F5BDE28225:FG=1; BDSFRCVID_BFESS=mduOJeC62rvsNQ7jSlVTU9Ok38g4MbJTH6f3Y9q_pPV_qG9fDYcCEG0PaM8g0Kub1DMtogKKL2OTHmuF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tJIJ_ID2JCD3enTmbt__-P4DeUcb-xRZ5mAqotoK-hrGMncbhhjx3jFgMN-OK53uKeQnaIQDtMIBqf7x0hjrKfb-b4Ok5MJ43bRT3lCy5KJvfJ_lQMcMhP-UyPkHWh37a6TlMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMonLafJOKHIClD5uBDxa; BA_HECTOR=a4a10124008hag000gal73l31hlqhgp1b; ZFY=Ppbkz99J6k5Hbe9YC7MvSARqGb6:BjY6aFsPIrJDMi:BI:C; RT="sl=0&ss=l9u2oaxi&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&z=1&dm=baidu.com&si=pkxa39d65w&ul=4y4o',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'referer': 'https://haokan.baidu.com/web/search/page?query=欧美电影'
}
headers = {'cookie':'BIDUPSID=8FC47947011F57D9176BCA81E2579A7E; PSTM=1665110861; BAIDUID=8FC47947011F57D9B1BD66F5BDE28225:FG=1; H_WISE_SIDS=110085_204427_204916_209568_210321_212295_212740_212868_213039_213360_214796_215730_216845_216941_217168_218549_219245_219565_219942_219946_220017_220663_221479_221795_221874_222299_222425_222625_223064_223211_223683_223906_224046_224077_224086_224159_224456_224633_225564_225593_225764_225846_225860_226006_226102_226270_226550_226628_226718_226815_226965_227063_227187_227515_227528_227747_227865_227869_227932_227941_227973_228138_228369_228380_228424_228507_228774_228807_228833_228978_229029_229033_229062_229125_229154_229286_229411_229525_229685_229750_229914_229918_229938_229967_230020_230040_230089_230237_230240_230244_230249_230305_230437_230468_230544_230686_230707_230861_230911_230930; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDSFRCVID=mduOJeC62rvsNQ7jSlVTU9Ok38g4MbJTH6f3Y9q_pPV_qG9fDYcCEG0PaM8g0Kub1DMtogKKL2OTHmuF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tJIJ_ID2JCD3enTmbt__-P4DeUcb-xRZ5mAqotoK-hrGMncbhhjx3jFgMN-OK53uKeQnaIQDtMIBqf7x0hjrKfb-b4Ok5MJ43bRT3lCy5KJvfJ_lQMcMhP-UyPkHWh37a6TlMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMonLafJOKHIClD5uBDxa; BDUSS=dtV000TVE1d210Z1VMZnduZEJHUm1HM24tdjFETWNWVFlTYnNTTDFheGphWU5qSVFBQUFBJCQAAAAAAAAAAAEAAAA5mBxx7bntue257bntue25MQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGPcW2Nj3FtjNX; BDUSS_BFESS=dtV000TVE1d210Z1VMZnduZEJHUm1HM24tdjFETWNWVFlTYnNTTDFheGphWU5qSVFBQUFBJCQAAAAAAAAAAAEAAAA5mBxx7bntue257bntue25MQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGPcW2Nj3FtjNX; H_PS_PSSID=26350; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1666330671,1667054298; hkpcSearch=%u6B27%u7F8E%u7535%u5F71%24%24%24%u6B27%u7F8E; PC_TAB_LOG=video_details_page; COMMON_LID=48664518cf6f29d4bc6ef0499309effd; ab_sr=1.0.1_NmY3YjA2MDViZTIzZjIyMmY3MGM1NWZkZjdiZjA3NDU0NWEyMjY2OTY5MmE0MDgzNTE1Mjg1M2JmNDI1M2QwMGY4YjE1MzE5ZmJiNWU4MDYwODJmMzBjZjk0OGI4OWE4YjE5ODIxMmQyNmEwMjEwOTVlOGZkMzA3YjNkZjJkNzE2OTQ1ZWNiNWZlZTBmNmVjYzkzNGUxZThhOWIwMDlkZg==; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1667056994; reptileData=%7B%22data%22%3A%22a4925e90b6e2dc93225045e44f90e728521c8d354952f17d4325d19acb9b59b7efdc9004ed0ab0201593cdb7eea807c27d662dd79cc272dc12faf2ad7e75d834db50303a31995e3cb2b97d683e762e62926f7c54d430687dd30ffb64288ffa95%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%22afe14bb0%22%7D; delPer=0; PSINO=5; BAIDUID_BFESS=8FC47947011F57D9B1BD66F5BDE28225:FG=1; BDSFRCVID_BFESS=mduOJeC62rvsNQ7jSlVTU9Ok38g4MbJTH6f3Y9q_pPV_qG9fDYcCEG0PaM8g0Kub1DMtogKKL2OTHmuF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tJIJ_ID2JCD3enTmbt__-P4DeUcb-xRZ5mAqotoK-hrGMncbhhjx3jFgMN-OK53uKeQnaIQDtMIBqf7x0hjrKfb-b4Ok5MJ43bRT3lCy5KJvfJ_lQMcMhP-UyPkHWh37a6TlMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMonLafJOKHIClD5uBDxa; BA_HECTOR=a4a10124008hag000gal73l31hlqhgp1b; ZFY=Ppbkz99J6k5Hbe9YC7MvSARqGb6:BjY6aFsPIrJDMi:BI:C; RT="sl=0&ss=l9u2oaxi&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&z=1&dm=baidu.com&si=pkxa39d65w&ul=4y4o',

           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

response = requests.get(url=url,
                        # params=p,
                        headers=headers)
print(response.json())


