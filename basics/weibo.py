#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
import json

from lazysdk import lazyrequests


def component(
        oid: str
):
    """

    :param oid: 例如 1034:4847802505953295
    :return:
    """
    url = 'https://weibo.com/tv/api/component'
    params = {
        'page': f'/tv/show/{oid}'
    }
    data = json.dumps({
        "Component_Play_Playinfo":
            {
                "oid": oid
            }
    })
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "UOR=bbs.anjian.com,widget.weibo.com,bbs.anjian.com; XSRF-TOKEN=9v-cEJDO9QN5L0rukJPK7Aia; SUB=_2AkMUwQOHf8NxqwFRmPwUyWvrZY5_wwvEieKinfJcJRMxHRl-yT9jqlBZtRB6P0EtaMxzpKi7uLCcUxp6CoUBBy7R_Amw; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhSuR50GZyjHG1xqgW_9qn9; WBPSESS=BP4XMQoD7Z31Vf3tBPaOodL0VeImfusyVxH417zAhPIX2tyxQ7gkzwRVobe5D6ogJa_8EbBtG8-e07N3VnH0UJf8GTVfR5gsG4FdGKkAp8DTSdfUAgPkr6O8SubxJObOyNiwxJwpI2wCs0sukStBCl4oq3woblY7nHcfT4vMoPE=; _s_tentry=weibo.com; Apache=6823741051034.528.1671269652714; SINAGLOBAL=6823741051034.528.1671269652714; ULV=1671269652781:1:1:1:6823741051034.528.1671269652714:; PC_TOKEN=11e0e33bb2; UPSTREAM-V-WEIBO-COM=35846f552801987f8c1e8f7cec0e2230",
        "Host": "weibo.com",
        "Origin": "https://weibo.com",
        # "PAGE-REFERER": "/tv/show/1034:4847802505953295",
        "Referer": f"https://weibo.com/tv/show/{oid}?from=old_pc_videoshow",  # 必须
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0",
    }
    return lazyrequests.lazy_requests(
        method='POST',
        url=url,
        params=params,
        data=f'data={data}',
        headers=headers,
        return_json=True
    )


def feed_all_groups():
    """
    获取分组信息
    :return:
    """
    url = 'https://weibo.com/ajax/feed/allGroups'
    # params = {
    #     'is_new_segment': 1,
    #     'fetch_hot': 1
    # }
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        "Cookie": "UOR=bbs.anjian.com,widget.weibo.com,bbs.anjian.com; XSRF-TOKEN=9v-cEJDO9QN5L0rukJPK7Aia; SUB=_2AkMUwQOHf8NxqwFRmPwUyWvrZY5_wwvEieKinfJcJRMxHRl-yT9jqlBZtRB6P0EtaMxzpKi7uLCcUxp6CoUBBy7R_Amw; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhSuR50GZyjHG1xqgW_9qn9; _s_tentry=weibo.com; Apache=6823741051034.528.1671269652714; SINAGLOBAL=6823741051034.528.1671269652714; ULV=1671269652781:1:1:1:6823741051034.528.1671269652714:; UPSTREAM-V-WEIBO-COM=35846f552801987f8c1e8f7cec0e2230; WBPSESS=BP4XMQoD7Z31Vf3tBPaOodL0VeImfusyVxH417zAhPIEsZiqOZJ198kqqlIjqeTPNktnox02cjl1kz2XnkvmiSWhs2hATgv1q7NGCad16P7kd66dqMYBl4e39ajaB4pO",
        "Host": "weibo.com",
        "Referer": "https://weibo.com/newlogin?tabtype=weibo&gid=1028032388&openLoginLayer=0&url=https%3A%2F%2Fweibo.com%2F",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0",
        "X-Requested-With": "XMLHttpRequest"
    }
    return lazyrequests.lazy_requests(
        method='GET',
        url=url,
        # params=params,
        headers=headers,
        return_json=True
    )


if __name__ == '__main__':
    print(feed_all_groups())