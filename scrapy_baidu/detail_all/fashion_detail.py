#爬取热点新闻
from selenium import webdriver
import time, re, os
import hashlib
from scrapy_baidu.commom.news_mysql import read_item, create_src_item, read_all_item, read_detail_item
from scrapy_baidu.commom.send_detail import pre, oss_pic_pre, oss_video_pre
from scrapy_baidu.commom.news_mysql import update_flag, update_errflag
from scrapy_baidu.commom.download_src import download_pic, download_video

# //*[@id="root"]/div[2]/div[2]/div[1]/div/div/span[4]/a


def download_fashion_detail():
    hot_details = read_detail_item(2)  #1是新闻 5是娱乐
    hot = ''
    print(len(hot_details))
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    browser = webdriver.Chrome(options=option)

    try:
        for i in range(len(hot_details)):

            # option = webdriver.ChromeOptions()
            # option.add_argument('headless')
            # browser = webdriver.Chrome(options=option)

            # browser = webdriver.Chrome("D:\soft\py\Google\Chrome\Application\chromedriver.exe", options=option)
            hot = hot_details[i][1]
            type = hot_details[i][3]
            title = hot_details[i][2]
            # hot = 'https://www.toutiao.com/article/7153628217511887395/'
            # hot = 'https://www.toutiao.com/article/7153016817810866725/'
            # type = 1
            # title = '刚刚发布，10月13日上海疫情最新消息，昨日新增47例本土感染者'
            # title = '山西17条措施促注册会计师行业健康发展'
            print(hot)
            repeatId = hashlib.md5()

            repeatId.update(hot.encode('utf-8'))
            repeatid = repeatId.hexdigest()
            # print('repeatid', repeatid, repeatId)

            try:
                browser.get(hot) #热点
                browser.implicitly_wait(10)
                source_ele = ''
                source_ele = browser.find_element_by_class_name('name').text
                print(source_ele)

                time.sleep(0.3)
            except Exception as e:
                print(e)
                update_errflag(hot)  # 更新flag,未保存div（后续处理）
            try:
                href = re.findall('<div class="article-content">(.*?)</article></div>', browser.page_source, re.S)[0]
                source_update = re.findall('<h1>(.*?)</a></span></div>', href, re.S)
                href = href.replace('<h1>' + source_update[0] + '</a></span></div>', '')
            except Exception as e:
                href = ''

            pic_filePath = "D:\\pic_src\\"
            video_filePath = "D:\\video_src\\"
            #上传图片
            if href:
                # pic_html = re.findall('<div class="pgc-img"><img src="(.*?)" img_width=', href, re.S)
                pic_html = re.findall('<img src="(.*?)" img_width=', href, re.S)
                for pic in pic_html:
                    ori_pic = pic
                    pic = pic.replace('amp;', '')
                    #下载图片
                    fileName = download_pic(pic)
                    #上传图片
                    time.sleep(0.1)
                    os_path = oss_pic_pre(fileName, hot)
                    if os_path:
                        href = str(href).replace(ori_pic, os_path)
                        # href = re.sub(re.compile('<img src="'+os_path+'(.*?);">', re.S), '<img src="' + os_path + '" alt=""/>', href)
                    else:
                        # href = str(href).replace(ori_pic, '')
                        href = re.sub(re.compile('<img src="'+ori_pic+'(.*?);">', re.S), '', href)
                    #新建数据
                    create_src_item(ori_pic, os_path, 'picture')
                    #删除本地数据
                    os.remove(pic_filePath + fileName)

                video_html = re.findall('mediatype="video" src="(.*?)"></video>', href, re.S)

                for video in video_html:
                    ori_video = video
                    video = video.replace('amp;', '')
                    #下载视频
                    fileName = download_video(video)
                    time.sleep(0.1)
                    #上传视频
                    os_path = oss_video_pre(fileName, hot)
                    if os_path:
                        href = str(href).replace(ori_video, os_path)
                        href = href.replace('<video class="" playsinline="true" x5-playsinline="true" webkit-playsinline="true" mediatype="video" src="' + os_path + '"></video>',
                                            '<video controls><source src="' + os_path + '" type="video/mp4"></video>')
                    else:
                        # href = str(href).replace(ori_video, '')
                        href = re.sub(re.compile('<video class=(.*?)'+ori_video+'"></video>', re.S), '', href)
                    #新建数据
                    create_src_item(ori_video, os_path, 'video')
                    #删除本地数据
                    os.remove(video_filePath + fileName)

                if 'amp;' in href:
                    href = href.replace('amp;', '')

                # print(href)
                # with open("news_hot.txt", "w",encoding="utf-8") as f:
                #     f.write(href)
                href = href + '<br><p style="font-size:10px; color:rgb(191, 191, 191)">作品来源于%s平台，版权归作者所有。</p>' %source_ele
                # href = href.replace('"', '\\"')
                delte_xg = re.findall('<xg-bar class(.*?)</xg-mini-layer></div>', href, re.S)
                if delte_xg:
                    href = re.sub(re.compile('<xg-bar class(.*?)</xg-mini-layer></div>', re.S), '', href)
                delte_xg_div = re.findall('<div class="tt-video-box(.*?)>', href, re.S)
                # print(delte_xg_div)
                if delte_xg_div:
                    # href = re.sub(re.compile('<div class="tt-video-box(.*?)top: 0px; left: 0px;">', re.S), '', href)
                    href = href.replace('<div class="tt-video-box' + delte_xg_div[0] + '>', '')

                update_imgs = re.findall('<img src="(.*?)>', href, re.S)
                # print('update_img', update_imgs)
                for update_img in update_imgs:
                    # href = re.sub(re.compile('<img src="(.*?)>', href, re.S))
                    href = href.replace('<img src="' + update_img + '>', '<img src="' + update_img + '/>')

                del_imgs = re.findall('img_width="(.*?)/>', href, re.S)
                for del_img in del_imgs:
                    href = href.replace('img_width="' + del_img, ' alt=""')

                img_srcs = re.findall('<div class="pgc-img"><p><img src="(.*?)/></p>', href, re.S)
                for img_src in img_srcs:
                    href = href.replace('<p><img src="' + img_src + '/></p>', '<img src="' + img_src + '/>')


                imgp_srcs = re.findall('<img src="(.*?)/>', href, re.S)
                for imgp_src in imgp_srcs:
                    href = href.replace('<img src="' + imgp_src + '/>', '<p><img src="' + imgp_src + '/></p>')

                href = href.replace('<div class="pgc-img">', '')
                href = href.replace('<p class="pgc-img-caption"></p></div>', '')
                href = href.replace('<article class="syl-article-base tt-article-content syl-page-article syl-device-pc">', '')
                time.sleep(0.1)
                with open("../scrapy_toutiao/news_hot.txt", "w", encoding="utf-8") as f:
                    f.write(href)
                print(href)
                print('type', type)

                ret = pre(title, type, href, repeatid, hot, i) #内容上传
                time.sleep(0.5)
                update_flag(hot, href, source_ele) #更新flag,未保存div（后续处理）
                time.sleep(0.1)

            # browser.close() #关闭当前窗口
    except Exception as e:
        print(e)
        update_errflag(hot) #更新flag,未保存div（后续处理）

download_fashion_detail()