import os

import requests, re, json
import pprint
import subprocess

from scrapy_baidu.commom.save_video import save_b_url


def get_response(html_url):

    headers = {
        'referer': 'https://www.bilibili.com/',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'cookie': "_uuid=1067A7661-ECB4-AD2E-710F1-C4AF4B3AAB6E24367infoc; buvid3=071E1FB9-4E9D-F675-FC73-EBF71502698928738infoc; b_nut=1665148026; buvid4=32D190EC-D94D-99F9-16FD-9ED757EF4D9028738-022100721-xWrW9RW0SscAM03ESt7jBw==; i-wanna-go-back=-1; nostalgia_conf=-1; rpdid=|(J|)R|~Y))k0J'uYYYk~kkRu; fingerprint=18e7f6cc53ea2a07151e4a1640a9ba47; buvid_fp_plain=undefined; DedeUserID=3461573018389263; DedeUserID__ckMd5=934ad58300c1a47f; buvid_fp=f602e0dc2c822f7ea8fea740ef2a42db; b_ut=5; bsource=search_baidu; CURRENT_QUALITY=0; blackside_state=1; SESSDATA=b0c65761,1683285604,341f7*b2; bili_jct=cc245489510dd1d757d16e3393e0dbd9; innersign=1; sid=5hv47ae6; PVID=1; CURRENT_FNVAL=4048; b_lsid=37A102AD8_184522D0648; bp_video_offset_3461573018389263=725735660862832800",
    }

    response = requests.get(url=html_url, headers=headers)
    # print(response.text)
    return response


def get_video_info(html_url):
    response = get_response(html_url)
    # title = re.findall('<h1 title="(.*?)" class="video-title">', response.text)[0]
    # title = re.findall('<h1 title="(.*?)" class="video-title tit">', response.text)[0]
    # html_data = re.findall('<script>window.__playinfo__=(.*?)</script>', response.text)[0]
    # json_data = json.loads(response)
    # print(response.text)
    # print(response.json())
    response = response.json()
    data_detail = response.get('data').get('result')

    for data_line in data_detail:
        arcurl = data_line.get('arcurl')
        title = data_line.get('title')
        duration = data_line.get('duration')
        aid = data_line.get('aid')
        save_b_url(title, arcurl, aid, duration, type=9)
    # pprint.pprint(json_data)
    # audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
    # video_url = json_data['data']['dash']['video'][0]['baseUrl']
    # video_info = [title, audio_url, video_url]
    # return video_info
    # print(title)
    # print(audio_url)
    # print(video_url)



# url = 'https://api.bilibili.com/x/web-interface/search/type?__refresh__=true&_extra=&context=&page=3&page_size=42&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=%E6%AC%A7%E7%BE%8E%E8%A7%86%E9%A2%91&qv_id=FdLwYb7TzkyLv5TA67QH03vYJolhGEbY&category_id=&search_type=video&dynamic_offset=48'
# url = 'https://api.bilibili.com/x/web-interface/search/type?__refresh__=true&_extra=&context=&page=2&page_size=42&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=%E6%AC%A7%E7%BE%8E%E8%A7%86%E9%A2%91&qv_id=FdLwYb7TzkyLv5TA67QH03vYJolhGEbY&category_id=&search_type=video&dynamic_offset=24'
for i in range(1,1001):
    url = 'https://api.bilibili.com/x/web-interface/search/type?__refresh__=true&_extra=&context=&page='+str(i)+'&page_size=42&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=%E6%AC%A7%E7%BE%8E%E8%A7%86%E9%A2%91&qv_id=FdLwYb7TzkyLv5TA67QH03vYJolhGEbY&category_id=&search_type=video&dynamic_offset=' + str(24*(i-1))
    print(url)
    video_info = get_video_info(url)

# save(video_info[0], video_info[1], video_info[2])

# merge_data(video_info[0])