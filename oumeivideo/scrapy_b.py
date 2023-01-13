import hashlib
import os
import uuid

import requests, re, json
import pprint
import subprocess

from scrapy_baidu.commom.news_mysql import update_b_video_flag
from scrapy_baidu.commom.save_video import read_b_item
from scrapy_baidu.commom.send_detail import oss_video_pre, video_send

video_filePath = "D:\\video_src\\"
b_details = read_b_item()

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
    title = re.findall('<h1 title="(.*?)" class="video-title tit">', response.text)[0]
    html_data = re.findall('<script>window.__playinfo__=(.*?)</script>', response.text)[0]
    json_data = json.loads(html_data)
    # pprint.pprint(json_data)
    audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
    video_url = json_data['data']['dash']['video'][0]['baseUrl']
    video_info = [title, audio_url, video_url]
    return video_info
    print(title)
    print(audio_url)
    print(video_url)

def save(title, audio_url, video_url):
    # title = "".join(title.split())
    fileName = str(uuid.uuid4())
    #音频 response.content 二进制数据
    audio_content = get_response(audio_url).content
    #视频
    video_content = get_response(video_url).content
    with open(fileName + '.mp3', mode='wb') as f:
        f.write(audio_content)
    with open(fileName + '.mp4', mode='wb') as f:
        f.write(video_content)
    print('baocunwanbi')
    return fileName


def merge_data(video_name):
    print('kaishihecheng', video_name)
    # COMMAND = f'ffmpeg -i {video_name}.mp4 -i {video_name}.mp3 -c:v copy -c:a aac -strict experimental {video_name}output.mp4'
    # subprocess.Popen(COMMAND, shell=True)
    print('shipinghechengjieshu', video_name)
    com = f'C:\\Users\\vvv\Downloads\\ffmpeg-4.3.1-2021-01-01-essentials_build\\bin\\ffmpeg.exe -i "{video_name}.mp3" -i "{video_name}.mp4" -acodec copy -vcodec copy {video_filePath}{video_name}.mp4'
    print(com)
    os.system(com)

    # audio = ffmpeg.input(f'{video_name}.mp3')
    # video = ffmpeg.input(f'{video_name}.mp4')
    # print("合并视音频")
    # out = ffmpeg.output(video, audio, f'{video_name}out.mp4')
    # out.run()
    # os.remove(f'{video_name}.mp3')
    # os.remove(f'{video_name}.mp4')
    print("完成")
    return video_name + '.mp4'


for i in range(len(b_details)):

    title = b_details[i][1]
    url = b_details[i][10]
    target = b_details[i][3]
    video_time = b_details[i][7]
    type = b_details[i][8]

    if ':' in video_time:
        v_time = video_time.split(':')[-2]
        print(v_time)
        if int(v_time) < 5 and type == 9:

            video_info = get_video_info(url)

            title = save(video_info[0], video_info[1], video_info[2])

            video_name = merge_data(title)

            #上传视频
            os_path = oss_video_pre(video_name,1)
            #post 视频
            repeatid = hashlib.md5()
            repeatid.update(url.encode('utf-8'))
            repeatid = repeatid.hexdigest()
            print(repeatid)
            tagId = 3
            video_send(title, os_path, repeatid, tagId)
            update_b_video_flag(url)
            os.remove(video_name)
            os.remove('C:\\Users\\vvv\PycharmProjects\\news_jot\Bzhan\\*.mp3')
            print(os.listdir(os.getcwd()))

# url = 'https://www.bilibili.com/video/BV1Cf4y1b7nD/?spm_id_from=333.337.search-card.all.click&vd_source=fcc6c656a573cc58ce2c2230e24b9e9a'
# url = 'https://www.bilibili.com/video/BV1b7411r7Ti/?spm_id_from=333.337.search-card.all.click'
#
#
# video_info = get_video_info(url)
#
# save(video_info[0], video_info[1], video_info[2])
#
# merge_data(video_info[0])