import requests,re

# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}   # 用户代理设置
headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'}   # 用户代理设置

# url = 'https://news.baidu.com/'
# url = 'https://news.baidu.com/news#/'
# url = 'https://news.baidu.com/news?fr=mohome&$pubpathUnescape#/'
url = 'https://news.baidu.com/news?fr=mohome&$pubpathUnescape#/newslist/widthNav/info/%E8%B4%A2%E7%BB%8F'
res = requests.get(url, headers=headers).text  # 使用浏览器的用户代理向网站发送访问请求
print(res)

# 获取信息的网址
p_href = '<li class="bold-item"><a href="(.*?)</a>'
href = re.findall(p_href, res)
# print(href)

# 获取信息的标题
# p_title = '<h2 class="news-title_1YtI1">.*?>(.*?)</a>'
# p_title = '<li class="bold-item">.*?>(.*?)</a>'
# p_title = 'target="_blank" mon="a=9">(.*?)</a>'
# title = re.findall(p_title, res, re.S)
# print(title)

for i in href:
    print(i)