import requests,re

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}   # 用户代理设置

# url = 'https://news.baidu.com/news?fr=mohome&$pubpathUnescape#/newslist/widthNav/info/%E8%B4%A2%E7%BB%8F'
# url = 'https://news.baidu.com/'
url = 'https://news.baidu.com/guonei'
res = requests.get(url, headers=headers).text  # 使用浏览器的用户代理向网站发送访问请求
# print(res)

# p_href = '<div class="index-module_articleWrap_2Zphx ">(.*?)</div>'
# p_href = r'(?:<div class="index-module_articleWrap_2Zphx ">)(.*)(?:</div>)'
# p_href = '<li><a href="(.*?)" class="title" (.*?)</a>'
# p_href = r'(?:<li><a href="http://)(.*)(?:</li>)'
p_href = r'(?:<ul class="ulist mix-ulist">)(.*)(?:</ul>)'
p_href = r'(?:<li><a href="http://)(.*)(?:</li>)'
# p_href = r'(?:<ul class="ulist)(.*)(?:</ul>)' ##used
# p_href = '<ul class="ulist "  >(.*?)</ul>'
href = re.findall(p_href, res, re.S)

print(href)
#
# patter = re.compile(r'ul(.*?)')
# for line in patter.findall(res):
#     print(line)


for i in href:
    # print(i)
    with open("2222.txt","w",encoding="utf-8") as f:
        f.write(i)

patter = r'(?:<li><a href="http://)(.*)(?:</li>)'

# res = re.findall(p_href, href[0], re.S)
res = re.findall(p_href, href[0])
print(res)

for i in res:
    # print(i)
    with open("333.txt","w",encoding="utf-8") as f:
        f.write(i)

# import requests
import re
from pyquery import PyQuery as pq
import json
# def get_one_page():
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
#         'Cookie':'BAIDUID=0F62A8857C7A1CDB9F058D43655C2A2C:FG=1; BAIDUID_BFESS=0F62A8857C7A1CDB9F058D43655C2A2C:FG=1; Hm_lvt_0c8070895132126fa3ba3bb7df1ac58e=1665145812; Hm_lpvt_0c8070895132126fa3ba3bb7df1ac58e=1665145812'
#
#     }
#     response = requests.get('https://news.baidu.com/news?fr=mohome&$pubpathUnescape#/newslist/widthNav/info/%E8%B4%A2%E7%BB%8F',headers=headers)
#     print(response.text)
#     if response.status_code == 200:
#         return response
#     return None
#
#
# def main():
#     # base_url = 'https://lens.zhihu.com/api/v4/videos/'#这个网址是通过分析得到，这一类视频的url都有一样的前缀。
#     url='https://news.baidu.com/news?fr=mohome&$pubpathUnescape#/newslist/widthNav/info/%E8%B4%A2%E7%BB%8F' #要爬取的《黄金单身汉》的网址
#     # appurl = re.match('^https://.*?(\d+)',url).group(1)  #提取出最后的数字1021147135768739840
#     # realurl = base_url+appurl  #拼接成真实的请求网址：https://lens.zhihu.com/api/v4/videos/1021147135768739840
#     html = get_one_page()#获取到真实网址的源代码，里面包含我们想要下载的视频的目的url
#     # url1 = json.loads(html.text)
#     # player_url = url1['playlist']['LD']['play_url'] #得到视频的url
#     #
#     # vidio = get_one_page(player_url)#爬取视频
#
#
#
#
# main()
