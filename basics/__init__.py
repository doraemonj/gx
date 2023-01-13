#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
from lazysdk import lazyrequests
import envx
api_env_file_name = 'local.gx_api.env'
api_env_info = envx.read(api_env_file_name)


def api_login():
    """
    登录api接口，拿到token
    :return:
    {
        'code': 0,
        'message': '成功',
        'data': {
            'passport': 'xxx',
            'name': 'xxx',
            'id': 10,
            'token': 'xxx'
        }
    }
    """
    url = "https://laiteinfo.com/gx_manager/manager/crawler/login"
    params = {
        "username": api_env_info['username'],
        "password": api_env_info['password']
    }
    return lazyrequests.lazy_requests(
        method='POST',
        url=url,
        json=params,
        verify=False,  # 不验证证书
        return_json=True
    )


def get_api_token():
    """
    获取api登录后的token
    :return:
    """
    login_res = api_login()
    if login_res['code'] == 0:
        return login_res['data']['token']
    else:
        return


def get_crawler_publish_users(
        token
):
    """
    新的虚拟号获取接口
    :param token:
    :return:
    """
    url = "https://laiteinfo.com/gx_manager/mission/getCrawlerPublishUsers"
    headers = {
        'x-auth-token': token
    }
    return lazyrequests.lazy_requests(
        method='GET',
        url=url,
        headers=headers,
        verify=False,  # 不验证证书
        return_json=True
    )


def mission_insert(
        token,
        content_attr: str,
        title: str,
        tag_id: int,
        user_id,
        repeat_id,
        source_platform: str = '微博'

):
    """
    插入数据到 大时代
    :param token:
    :param content_attr:
    :param title:
    :param tag_id:
    :param user_id:
    :param repeat_id:
    :param source_platform: 来源平台
    :return:
    """
    url = "https://laiteinfo.com/mission/insert"
    headers = {
        'x-auth-token': token
    }
    platform_mark = f"""<p style="text-align: justify; font-size: 18px; text-indent: 0em;">
	<span style="color: rgb(217, 217, 217); font-size: 12px;">本作品来源于{source_platform}平台，版权归创作者所有。</span>
</p>"""
    content_attr = content_attr.replace('text-align:  center', 'text-align:center') + platform_mark  # 重新排版
    data = {
        "type": "",
        "isWaterMark": False,
        "content": "",
        "contentAttr": content_attr,
        "title": title,
        "accessoryType": "",
        "accessorys": [],
        "lat": 31.30321580717796,
        "lng": 120.59294231967466,
        "location": "",
        "topicName": [],
        "tagId": tag_id,
        "status": 1,
        "userId": user_id,
        "repeatId": repeat_id
    }
    return lazyrequests.lazy_requests(
        method='POST',
        url=url,
        headers=headers,
        json=data,
        verify=False,  # 不验证证书
        return_json=True
    )


def pic_up2_oss(
        file_dir
):
    """
    上传图片到oss,此接口无需鉴权
    :param file_dir:
    :return:
    成功返回：
    {
        "code": 0,
        "message": "成功",
        "data": [
            "http://..."
        ]
    }
    """
    files = {'file': open(file_dir, 'rb')}
    return lazyrequests.lazy_requests(
        method='POST',
        url='https://laiteinfo.com/user/oss/uploads',
        files=files,
        verify=False,  # 不验证证书
        return_json=True
    )


def video_up2_oss(
        file_dir
):
    """
    上传视频到oss,此接口无需鉴权
    :param file_dir:
    :return:
    正确返沪：{'code': 0, 'message': '成功', 'data': 'http://l...0.mp4'}
    """
    files = {'file': open(file_dir, 'rb')}
    return lazyrequests.lazy_requests(
        method='POST',
        url='https://laiteinfo.com/admin/vod/video/upload',
        files=files,
        verify=False,  # 不验证证书
        return_json=True
    )


def make_video_html(
        poster_url: str = None,
        video_url: str = None
):
    """
    生成视频html代码
    :param poster_url: 封面图地址
    :param video_url: 视频文件地址
    :return:
    """
    html = f"""
<p>
    <video controls poster="{poster_url}">
        <source src="{video_url}" type="video/mp4">
    </video>
</p>
    """
    return html


def get_type_mapper():
    """
    获取频道
    :return:
    """
    url = "https://laiteinfo.com/mission/getTypeMapper"
    return lazyrequests.lazy_requests(
        method='GET',
        url=url,
        verify=False,  # 不验证证书
        return_json=True
    )


def video_upload(
        desc: str,
        video_url: str,
        proportion: str,
        tag_id,
        user_id,
        repeat_id,
        token
):
    """
    插入短视频
    :param desc: 描述
    :param video_url:
    :param proportion: 宽高比，例如 1920:1080
    :param tag_id:
    :param user_id:
    :param repeat_id:
    :param token:
    :return:
    """
    url = "https://laiteinfo.com/video/upload"
    headers = {
        'x-auth-token': token
    }
    data = {
        "desc": desc,
        "url": video_url,
        "proportion": proportion,
        "visible": 1,
        "location": "",
        "cityName": "",
        "tagId": tag_id,
        "userId": user_id,
        "missionTagId": "",
        "repeatId": repeat_id
    }
    print(data)
    return lazyrequests.lazy_requests(
        method='POST',
        url=url,
        json=data,
        headers=headers,
        verify=False,  # 不验证证书
        return_json=True
    )

if __name__ == '__main__':
    print(get_type_mapper())