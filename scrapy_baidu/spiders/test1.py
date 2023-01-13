#!/usr/bin/python
# -*- coding:utf-8 -*-

import httplib


class NewsBaidu(object):

    def __init__(self):
        super(NewsBaidu,self).__init__()

    def request(self):
        conn = httplib.HTTPConnection('news.baidu.com')  #请求的host
        request_url = '/'                                #请求的网页路径
        body = ''										 #请求的参数
        headers = {}									 #请求所带的头信息，该参数是一个字典
        conn.request('GET',request_url,body,headers)
        result = conn.getresponse()
        print('获取百度新闻')
        print(result.status)
        print(result.reason)

if __name__ == '__main__':
    nb = NewsBaidu()
    nb.request()