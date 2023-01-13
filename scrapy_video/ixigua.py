#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
import easydownload
import lazysdk.lazyrequests
from lazysdk import lazymd5
from lazymedia import ixigua
import showlog
import fastmongo
from basics import video_up2_oss
import basics
import os
import pymediainfo
import random

env_file_name_mongo = 'local.mongo.env'
tag_id = 9  # 原来代码是3-影视，ethan(刘岩)要求改9

# 获取token以及虚拟号
temp_token = basics.get_api_token()
print('temp_token', temp_token)
user_id_dic = basics.get_crawler_publish_users(temp_token)
user_list = user_id_dic.get('data')

# 随机拿一个虚拟号
random_user_id = random.choice(user_list)['userId']
search_keyword = '欧美'


def get_info():
    showlog.info('正在获取搜索结果...')

    page = 1
    while True:
        showlog.info(f'正在采集第 {page} 页的信息...')
        search_res = ixigua.search(
            keyword=search_keyword,
            page=page,
            page_size=10
        )
        if search_res['code'] == 0:
            data = search_res['data']
            has_more = data['has_more']
            inner_data = data['data']
            temp_res = list()
            for each_inner_data in inner_data:
                temp_data = each_inner_data['data']
                temp_data['type'] = each_inner_data['type']
                temp_data['search_keyword'] = search_keyword
                temp_res.append(temp_data)
            showlog.info(f'共获取到 {len(temp_res)} 条数据，正在保存结果...')
            fastmongo.safe_upsert(
                values=temp_res,
                db='ixigua',
                collection='search_res',
                env_file_name=env_file_name_mongo,
                query_keys=['search_keyword', 'group_id']
            )
            if has_more:
                page += 1
            else:
                break


def main():
    showlog.info('正在获取采集到的西瓜平台的信息...')
    tasks = fastmongo.safe_find(
        query={
            "mission_insert_state": {'$eq': None},
            "search_keyword": search_keyword
        },
        db='ixigua',
        collection='search_res',
        env_file_name=env_file_name_mongo,
    )
    showlog.info(f'获取到 {len(tasks)} 条记录...')
    for task_index, task_info in enumerate(tasks):
        showlog.info(f'正在遍历第 {task_index+1}/{len(tasks)} 条记录...')
        group_id = task_info['group_id']
        title = task_info['title']
        media_page_url = f'https://www.ixigua.com/{group_id}'
        repeat_id = lazymd5.md5_str(media_page_url)
        showlog.info('正在解析视频...')
        ana_res = lazysdk.lazyrequests.lazy_requests(
            method='POST',
            url='https://mediabug.photonreading.com/api/media/analyze',
            json={
                "content": media_page_url
            },
            return_json=True
        )
        if ana_res['code'] == 0:
            showlog.info('解析成功')
            file_url = ana_res['url']
            print(file_url)
            showlog.info('正在下载...')
            download_res = easydownload.safe_download(
                url=file_url,size_limit=80*1024*1024
            )

            if download_res:
                print(download_res)
                video_info = pymediainfo.MediaInfo.parse(filename=download_res)
                if video_info.tracks:
                    showlog.warning('下载失败')
                    continue
                else:
                    pass
                print('video_info:', video_info)
                video_track = video_info.tracks[1].to_data()
                video_width = video_track['width']
                video_height = video_track['height']
                video_proportion = f'{video_width}:{video_height}'  # 宽高比
                showlog.info('下载完成，正在上传至oss...')
                up2_oss_res = video_up2_oss(
                    file_dir=download_res
                )
                print(up2_oss_res)
                os.remove(download_res)
                if up2_oss_res['code'] == 0:
                    file_oss_url = up2_oss_res['data']
                    showlog.info('上传成功，正在推送到接口...')
                    video_upload_res = basics.video_upload(
                        desc=title,
                        video_url=file_oss_url,
                        proportion=video_proportion,
                        tag_id=tag_id,
                        user_id=random.choice(user_list)['userId'],
                        repeat_id=repeat_id,
                        token=temp_token
                    )
                    if video_upload_res['code'] == 0:
                        showlog.info('推送成功，正在更新状态...')
                        task_info['mission_insert_state'] = True
                        fastmongo.safe_upsert(
                            values=[task_info],
                            db='ixigua',
                            collection='search_res',
                            env_file_name=env_file_name_mongo,
                            query_keys=['search_keyword', 'group_id']
                        )
                        showlog.info('状态更新成功')
                    else:
                        showlog.warning('推送错误')
                        print(video_upload_res)
                        exit()
                else:
                    showlog.error('')
                    exit()
            else:
                showlog.info('下载失败，正在更新状态...')
                task_info['mission_insert_state'] = False
                task_info['mission_insert_msg'] = 'size too large'
                fastmongo.safe_upsert(
                    values=[task_info],
                    db='ixigua',
                    collection='search_res',
                    env_file_name=env_file_name_mongo,
                    query_keys=['search_keyword', 'group_id']
                )
                showlog.info('状态更新成功')

        else:
            showlog.warning('解析失败')


if __name__ == '__main__':
    get_info()
    main()

