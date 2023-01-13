
import requests



headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Hera-BD00; HMSCore 6.7.0.322) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.1.3.303 Mobile Safari/537.36'
}

# url = 'https://news.baidu.com/news#/newslist/'
url = 'https://news.baidu.com/news?fr=mohome&$pubpathUnescape#/'

# res = requests.get(url, headers=headers)
res = requests.get(url, headers=headers).text

print(res)
