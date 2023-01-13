from lazysdk import lazyrequests
from lazysdk import lazyfile
from lazysdk import lazymd5
from lazysdk import lazytime
from lazysdk import lazydict
import fastmongo
import showlog
import basics
import random
import copy
import os
import re
from basics import weibo
import easydownload


env_file_name_mongo = 'local.mongo.env'
mongo_db = 'weibo'
mongo_collection = 'api_feed_hottimeline'
mongo_collection_feed_groups = 'feed_groups'

pic_headers = {
    "Accept": "image/avif,image/webp,*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Referer": "https://weibo.com/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0"
}  # 下载图片的headers
video_headers = {
    "Accept": "video/webm,video/ogg,video/*;q=0.9,application/ogg;q=0.7,audio/*;q=0.6,*/*;q=0.5",
    "Accept-Encoding": "identity",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Connection": "keep-alive",
    "Referer": "https://weibo.com/",
    "Sec-Fetch-Dest": "video",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "cross-site",
    "TE": "trailers",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0"
}  # 下载视频的headers

temp_token = basics.get_api_token()
print('temp_token', temp_token)
user_id_dic = basics.get_crawler_publish_users(temp_token)
user_list = user_id_dic.get('data')


def feed_hot_time_line(
        refresh: int = 2,
        group_id: int = 1028032388,
        group_name: str = '动漫',
        container_id: str = '102803_ctg1_2388_-_ctg1_2388',
        ext_param: str = 'discover|new_feed',
        page: int = 1,
        page_size: int = 10
):
    """
    微博分类热门信息接口
    :param refresh: 默认为2，原来是1，应该是固定值
    :param group_id: gid, 1028032388：热门微博-动漫
    :param group_name: title
    :param container_id: containerid
    :param ext_param: 相对固定的
    :param page:
    :param page_size:
    :return:
    """
    url = 'https://weibo.com/ajax/feed/hottimeline'
    params = {
        'refresh': refresh,
        'group_id': group_id,
        'containerid': container_id,
        'extparam': ext_param,
        'max_id': page - 1,
        'count': page_size
    }
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        "Cookie": "UOR=bbs.anjian.com,widget.weibo.com,bbs.anjian.com; XSRF-TOKEN=9v-cEJDO9QN5L0rukJPK7Aia; PC_TOKEN=819a265a31; SUB=_2AkMUwQOHf8NxqwFRmPwUyWvrZY5_wwvEieKinfJcJRMxHRl-yT9jqlBZtRB6P0EtaMxzpKi7uLCcUxp6CoUBBy7R_Amw; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhSuR50GZyjHG1xqgW_9qn9; WBPSESS=BP4XMQoD7Z31Vf3tBPaOodL0VeImfusyVxH417zAhPIX2tyxQ7gkzwRVobe5D6ogAIRmhj8WMZMDaIvFgzGjn4QrJRgm57L0YwicYESeF1M8bUbMhqg6zk6Ex8bsz2D__9YHfGyiz8SM0BFG-AJ84gVHe29WFhTNGat_eBIbROk=; _s_tentry=weibo.com; Apache=6823741051034.528.1671269652714; SINAGLOBAL=6823741051034.528.1671269652714; ULV=1671269652781:1:1:1:6823741051034.528.1671269652714:",
        "Referer": "https://weibo.com/newlogin?tabtype=weibo&gid=1028032388&openLoginLayer=0&url=https%3A%2F%2Fweibo.com%2F",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0",
        "X-Requested-With": "XMLHttpRequest",
        "X-XSRF-TOKEN": "9v-cEJDO9QN5L0rukJPK7Aia",
        "client-version": "v2.37.13",
        "server-version": "v2022.12.16.2",
        "traceparent": "00-ec728af4ea08a496a9dc1423de16cdd6-03ac78a4b834c3cd-00"
    }
    return lazyrequests.lazy_requests(
        method='GET',
        url=url,
        params=params,
        headers=headers,
        return_json=True
    )


def get_all(
        group_id: int,  # 微博频道id
        group_name: str,
        container_id: str,
        limit: int = 100
):
    # group_id = 1028032388
    # group_name = '动漫'
    page = 1
    data_count = 0
    while True:
        showlog.info(f'正在获取第 {page} 页的数据...')
        response = feed_hot_time_line(
            page=page,
            page_size=10,
            group_id=group_id,
            group_name=group_name,
            container_id=container_id,
            ext_param='discover|new_feed'
        )
        statuses = response.get('statuses')  # 数据list
        total_number = response.get('total_number')  # 总数量
        max_id = response.get('max_id')
        if statuses:
            for statuse in statuses:
                # 以mid为主键
                statuse['group_id'] = group_id
                statuse['group_name'] = group_name
            showlog.info(f'获取到 {len(statuses)} 条记录，正在存储...')
            fastmongo.safe_upsert(
                values=statuses,
                db=mongo_db,
                collection=mongo_collection,
                env_file_name=env_file_name_mongo,
                query_keys=['group_id', 'mid']
            )
            showlog.info('存储完成')
            page += 1
            data_count += len(statuses)
            if data_count >= limit:
                showlog.info('达到采集数量限制')
                return data_count
        else:
            showlog.info('采集结束')
            print(response)
            return 0


def clean_data(
        group_id: int,  # 微博频道id
        tag_id: int,  # 发不到大时代的id
        limit=100,
):
    showlog.info('正在获取采集到的记录...')
    all_data = fastmongo.safe_find(
        query={
            "mission_insert_state": {'$eq': None},
            "group_id": group_id
        },
        sort_setting=[('_id', -1)],
        db=mongo_db,
        collection=mongo_collection,
        env_file_name=env_file_name_mongo,
        limit_num=limit
    )
    showlog.info(f'获取到 {len(all_data)} 条记录...')
    for data_index, each_data in enumerate(all_data):
        html_item = ''  # 生成发布内容
        showlog.info(f'正在处理第 {data_index+1}/{len(all_data)} 条记录...')
        print(each_data)
        text_raw = each_data['text_raw']
        mid = each_data['mid']
        mid_md5 = lazymd5.md5_str(content=str(mid))  # 生成重复识别id
        each_data['mid_md5'] = mid_md5
        if 'http' in text_raw:
            text_raw_process = text_raw.split('http')[0]  # 这个步骤不知道干嘛的，先照抄了
        else:
            text_raw_process = text_raw
        each_data['text_raw_process'] = text_raw_process
        each_data['mission_insert_state'] = False
        if 0 < len(text_raw_process) < 30:
            pic_ids = each_data.get('pic_ids')  # 每张图片的id组成的list
            pic_infos = each_data.get('pic_infos')  # 每张图片的信息，用id作key提取
            page_info = each_data.get('page_info')
            pic_gx_oss = dict()  # 转存到oss
            if pic_ids:
                for pic_id_index, pic_id in enumerate(pic_ids):
                    showlog.info(f'正在处理第 {pic_id_index+1}/{len(pic_ids)} 张图片')
                    pic_info = pic_infos[pic_id]  # 单个图片信息
                    original_url = pic_info.get('original').get('url')
                    showlog.info('正在下载...')
                    while True:
                        try:
                            download_res = easydownload.safe_download(
                                url=original_url,
                                headers=pic_headers
                            )  #
                            break
                        except:
                            continue
                    file_dir = download_res
                    showlog.info('下载完成')
                    showlog.info('正在上传到oss...')
                    up2_oss_res = basics.pic_up2_oss(file_dir=file_dir)
                    print(up2_oss_res)
                    os.remove(file_dir)
                    if up2_oss_res['code'] == 0:
                        file_oss_url = up2_oss_res['data'][0]
                        pic_gx_oss[pic_id] = file_oss_url
                        html_item = html_item + '<p><img src="' + file_oss_url.split('?')[0] + '" alt=""/></p>'
                    else:
                        showlog.error('')
                        exit()
            each_data['gx_oss_pic'] = pic_gx_oss
            if page_info:
                media_info = page_info.get('media_info')
                url_struct = each_data.get('url_struct')
                if media_info and url_struct:
                    oid = url_struct[0]['actionlog']['oid']
                    showlog.info('正在获取视频的文件地址信息...')
                    component_res = weibo.component(oid=oid)
                    print(component_res)
                    Component_Play_Playinfo = component_res['data']['Component_Play_Playinfo']
                    if Component_Play_Playinfo:
                        urls = Component_Play_Playinfo['urls']
                        cover_image = Component_Play_Playinfo['cover_image']  # 封面图
                        max_defi = 0
                        # max_defi_limit = 720
                        max_url = ''
                        for defi, url in urls.items():
                            defi_num = re.findall(r' (.*?)P', defi, re.S)
                            if defi_num:
                                defi_num = int(defi_num[0])
                            else:
                                continue
                            if defi_num > max_defi:
                                max_url = url
                                max_defi = copy.deepcopy(defi_num)
                                # if max_defi >= max_defi_limit:
                                #     break
                        max_url = 'http:' + max_url
                        showlog.info(f'获取到最大分辨率为 {max_defi}P')
                        if 'live.video' in max_url and 'm3u8' in max_url:
                            showlog.warning('直播流为m3u8，暂不下载')
                        else:

                            media_gx_oss = dict()  # 转存到oss
                            print('media_info', media_info)

                            showlog.info('正在下载视频...')
                            while True:
                                try:
                                    download_res = easydownload.safe_download(
                                        url=max_url,
                                        headers=video_headers
                                    )
                                    break
                                except:
                                    continue
                            video_file_dir = download_res
                            showlog.info('下载完成')
                            showlog.info('正在上传到oss...')
                            video_up2_oss_res = basics.video_up2_oss(file_dir=video_file_dir)
                            print(video_up2_oss_res)
                            os.remove(video_file_dir)
                            if video_up2_oss_res['code'] == 0:
                                media_gx_oss['video'] = video_up2_oss_res['data']
                                video_oss_html = video_up2_oss_res['data'].split('?')[0]
                            else:
                                showlog.warning('上传至oss失败')
                                exit()

                            showlog.info('正在下载封面图...')
                            while True:
                                try:
                                    download_cover_image = easydownload.safe_download(
                                        url='http:' + cover_image,
                                        headers=pic_headers
                                    )
                                    break
                                except:
                                    continue
                            cover_image_file_dir = download_cover_image
                            showlog.info('下载完成')
                            showlog.info('正在上传到oss...')
                            cover_image_up2_oss_res = basics.pic_up2_oss(file_dir=cover_image_file_dir)
                            print(cover_image_up2_oss_res)
                            os.remove(cover_image_file_dir)
                            if cover_image_up2_oss_res['code'] == 0:
                                media_gx_oss['cover_image'] = cover_image_up2_oss_res['data'][0]
                                cover_image_oss_html = cover_image_up2_oss_res['data'][0].split('?')[0]
                            else:
                                showlog.warning('上传至oss失败')
                                exit()
                            html_item += basics.make_video_html(
                                poster_url=cover_image_oss_html,
                                video_url=video_oss_html
                            )
                            each_data['gx_oss_media'] = media_gx_oss
                    else:
                        each_data['mission_insert_msg'] = f'无法获取视频信息：{component_res}'
                else:
                    pass


            if html_item:
                showlog.info('正在推送内容到大时代接口')
                random_user_index = random.randint(0, len(user_list)-1)
                random_user = user_list[random_user_index]
                random_user_id = random_user['userId']
                # tag_id = 10  # 动漫这个是10
                mission_insert_res = basics.mission_insert(
                    token=temp_token,
                    content_attr=html_item,
                    title=text_raw_process,
                    tag_id=tag_id,
                    user_id=random_user_id,
                    repeat_id=mid_md5,  # 可能是用来识别是否重复的
                    source_platform='微博'
                )
                print('mission_insert_res', mission_insert_res)
                each_data['mission_insert_state'] = True
                each_data['mission_insert_user_id'] = random_user_id
                each_data['mission_insert_tag_id'] = tag_id
                datetime_now = lazytime.get_datetime()
                each_data['mission_insert_datetime'] = datetime_now
                each_data['mission_insert_date'] = lazytime.get_datetime2date(datetime_now)
            else:
                showlog.warning('无要上传的内容')
                if each_data.get('mission_insert_msg'):
                    pass
                else:
                    each_data['mission_insert_msg'] = 'html_item is empty'
        else:
            showlog.warning('text_raw_process is too long')
            each_data['mission_insert_msg'] = 'text_raw_process is too long'
        showlog.info('正在更新标记...')
        fastmongo.safe_upsert(
            values=[each_data],
            db=mongo_db,
            collection=mongo_collection,
            env_file_name=env_file_name_mongo,
            query_keys=['group_id', 'mid']
        )
        showlog.info('标记更新完成')


def get_feed_all_groups():
    """
    获取频道推荐的所有频道，获取一次就可以
    :return:
    """
    showlog.info('正在获取[频道推荐]...')
    feed_all_groups_res = weibo.feed_all_groups()
    all_group = list()
    for feed_group in feed_all_groups_res['groups']:
        feed_group_title = feed_group['title']
        this_group = feed_group['group']
        for each in this_group:
            each['father_title'] = feed_group_title
        all_group.extend(this_group)
    showlog.info('正在保存频道推荐信息...')
    fastmongo.safe_upsert(
        values=copy.deepcopy(all_group),
        db=mongo_db,
        collection=mongo_collection_feed_groups,
        query_keys=['gid', 'uid'],
        env_file_name=env_file_name_mongo
    )
    return all_group


def main():
    each_limit = 100
    showlog.info('正在获取频道列表...')
    type_mapper_res = basics.get_type_mapper()
    chance_type_mapper = type_mapper_res['data']['chance']
    print(chance_type_mapper)
    showlog.info(f'获取到 {len(chance_type_mapper)} 个分类...')
    chance_type_mapper_dict = lazydict.dict_list_group(
        list_in=chance_type_mapper,
        by='name'
    )
    showlog.info('正在获取微博频道列表...')
    weibo_feed_groups = get_feed_all_groups()
    showlog.info(f'获取到 {len(weibo_feed_groups)} 个微博频道')
    for each_feed_group in weibo_feed_groups:
        print(each_feed_group)
        feed_group_title = each_feed_group['title']
        feed_group_id = each_feed_group['gid']
        feed_group_containerid = each_feed_group.get('containerid')
        if feed_group_containerid:
            if feed_group_title in chance_type_mapper_dict.keys():
                chance_type_mapper_info = chance_type_mapper_dict[feed_group_title]
                chance_type_mapper_id = chance_type_mapper_info[0]['value']
                print('命中', feed_group_title, '-->', chance_type_mapper_id)
                showlog.info('正在采集数据...')
                get_all(
                    group_id=feed_group_id,
                    group_name=feed_group_title,
                    container_id=feed_group_containerid,
                    limit=each_limit
                )
                showlog.info('正在清洗数据...')
                clean_data(
                    group_id=feed_group_id,
                    tag_id=chance_type_mapper_id,
                    limit=each_limit
                )
        else:
            continue


if __name__ == '__main__':
    """
    微博共有67个频道，命中15个频道
    命中 情感 --> 4
    命中 美食 --> 23
    命中 时尚 --> 2
    命中 动漫 --> 10
    命中 国际 --> 9
    命中 旅游 --> 16
    命中 星座 --> 3
    命中 美女 --> 25
    命中 财经 --> 18
    命中 体育 --> 20
    命中 科技 --> 17
    命中 健康 --> 22
    命中 游戏 --> 6
    命中 汽车 --> 24
    命中 军事 --> 21
"""
    main()
