import hashlib, os

from selenium import webdriver
import time,re,json,base64

from scrapy_baidu.commom.download_src import download_video
from scrapy_baidu.commom.news_mysql import process_item, update_video_flag, update_haokan_video_flag
from scrapy_baidu.commom.save_video import save_xigua, read_item, read_haokan_item
import requests

from scrapy_baidu.commom.send_detail import oss_video_pre, video_send

headers = {
    'cookie': 'BIDUPSID=8FC47947011F57D9176BCA81E2579A7E; PSTM=1665110861; BAIDUID=8FC47947011F57D9B1BD66F5BDE28225:FG=1; H_WISE_SIDS=110085_204427_204916_209568_210321_212295_212740_212868_213039_213360_214796_215730_216845_216941_217168_218549_219245_219565_219942_219946_220017_220663_221479_221795_221874_222299_222425_222625_223064_223211_223683_223906_224046_224077_224086_224159_224456_224633_225564_225593_225764_225846_225860_226006_226102_226270_226550_226628_226718_226815_226965_227063_227187_227515_227528_227747_227865_227869_227932_227941_227973_228138_228369_228380_228424_228507_228774_228807_228833_228978_229029_229033_229062_229125_229154_229286_229411_229525_229685_229750_229914_229918_229938_229967_230020_230040_230089_230237_230240_230244_230249_230305_230437_230468_230544_230686_230707_230861_230911_230930; BDUSS=dtV000TVE1d210Z1VMZnduZEJHUm1HM24tdjFETWNWVFlTYnNTTDFheGphWU5qSVFBQUFBJCQAAAAAAAAAAAEAAAA5mBxx7bntue257bntue25MQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGPcW2Nj3FtjNX; BDUSS_BFESS=dtV000TVE1d210Z1VMZnduZEJHUm1HM24tdjFETWNWVFlTYnNTTDFheGphWU5qSVFBQUFBJCQAAAAAAAAAAAEAAAA5mBxx7bntue257bntue25MQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGPcW2Nj3FtjNX; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1666330671,1667054298; hkpcSearch=%u6B27%u7F8E%u7535%u5F71%24%24%24%u6B27%u7F8E; PC_TAB_LOG=video_details_page; COMMON_LID=48664518cf6f29d4bc6ef0499309effd; BAIDUID_BFESS=8FC47947011F57D9B1BD66F5BDE28225:FG=1; ZFY=Ppbkz99J6k5Hbe9YC7MvSARqGb6:BjY6aFsPIrJDMi:BI:C; delPer=0; PSINO=5; BCLID=8279814679575894301; BCLID_BFESS=8279814679575894301; BDSFRCVID=GkLOJexroG06EKOjDF8OU9Ok3eKKg9TTDYLEOwXPsp3LGJLVcjg-EG0Pt8i0Cou-dk83ogKKL2OTHmuF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=GkLOJexroG06EKOjDF8OU9Ok3eKKg9TTDYLEOwXPsp3LGJLVcjg-EG0Pt8i0Cou-dk83ogKKL2OTHmuF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=fR-f_D_5fIvDqTrP-trf5DCShUFs26ORB2Q-XPoO3Kt-sqvOMxOShq4AetnWJ-QiWKk8-UbgylRp8P3y0bb2DUA1y4vp5-TMHmTxoUJ2fnI2En7GqtOOe5tebPRiWTj9QgbLLlQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0bDP6j6Kbe5PVKgTa54cbb4o2WbCQQf-28pcN2b5oQTOBQtR9af3QaC5PVl7otb5vOn0w3hOUWfAkXpJvQnJjt2JxaqRCKbcJKq5jDh3Me-cQLUnte43Wfn7y0hvcBIocShnz5fjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQheHAftjDffn3aQ5rtKRTffjrnhPF3WqJ3XP6-hnjy3b4qKlvv2qbSsR6aefnODPLUyUt8Lp3RymJ42-39LPO2hpRjyxv4-PIsqtoxJpOJfIKj5b7aHRbObKOvbURvX5Dg3-7L-x5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEVCP5JD_bbKvPKITD-tFO5eT22-usyCOr2hcHMPoosItCQfRcMx0jbtJPqxRWtKTiab0XQUbUoqRHXnJi0btQDPvxBf7pKKQMsl5TtUJMbbIxLPnhqt0feabyKMniBnr9-pnEblQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuejAbj6jWeaRabK6aKC5bL6rJabC3snvsXU6q2bDeQN0q0xn92enlVp7Gfl7Ohn5oyPtB3h0vWtv4WbbvLT7johRTWqR4HncTqfonDh83eMuj3-RtHCnWVIOO5hvv8KoO3M7V5fKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRA8_K-53j; H_BDCLCKID_SF_BFESS=fR-f_D_5fIvDqTrP-trf5DCShUFs26ORB2Q-XPoO3Kt-sqvOMxOShq4AetnWJ-QiWKk8-UbgylRp8P3y0bb2DUA1y4vp5-TMHmTxoUJ2fnI2En7GqtOOe5tebPRiWTj9QgbLLlQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0bDP6j6Kbe5PVKgTa54cbb4o2WbCQQf-28pcN2b5oQTOBQtR9af3QaC5PVl7otb5vOn0w3hOUWfAkXpJvQnJjt2JxaqRCKbcJKq5jDh3Me-cQLUnte43Wfn7y0hvcBIocShnz5fjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQheHAftjDffn3aQ5rtKRTffjrnhPF3WqJ3XP6-hnjy3b4qKlvv2qbSsR6aefnODPLUyUt8Lp3RymJ42-39LPO2hpRjyxv4-PIsqtoxJpOJfIKj5b7aHRbObKOvbURvX5Dg3-7L-x5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEVCP5JD_bbKvPKITD-tFO5eT22-usyCOr2hcHMPoosItCQfRcMx0jbtJPqxRWtKTiab0XQUbUoqRHXnJi0btQDPvxBf7pKKQMsl5TtUJMbbIxLPnhqt0feabyKMniBnr9-pnEblQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuejAbj6jWeaRabK6aKC5bL6rJabC3snvsXU6q2bDeQN0q0xn92enlVp7Gfl7Ohn5oyPtB3h0vWtv4WbbvLT7johRTWqR4HncTqfonDh83eMuj3-RtHCnWVIOO5hvv8KoO3M7V5fKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRA8_K-53j; __bid_n=1843dd9428d2b6ddfd4207; BAIDU_WISE_UID=wapp_1667484959763_397; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; userFrom=null; BDRCVFR[K-_II4leN16]=mk3SLVN4HKm; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1667728209; ariaDefaultTheme=undefined; H_PS_PSSID=; BA_HECTOR=a124a18100aka480ag0g8u3i1hmf1ul1f; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; RT="sl=0&ss=la56bd14&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&z=1&dm=baidu.com&si=873022d8-e739-444b-a190-49bddd3af82f&ld=2msbmd&ul=u8ce&hd=u8vv"',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'host' : 'haokan.baidu.com',
}
video_filePath = "D:\\video_src\\"
haokan_details = read_haokan_item()

for i in range(len(haokan_details)):

    title = haokan_details[i][1]
    url = haokan_details[i][9]
    target = haokan_details[i][3]
    video_time = haokan_details[i][7]
    type = haokan_details[i][8]
    if ':' in video_time:
        if len(video_time.split(':')) == 2:
            print(video_time)
            v_time = video_time.split(':')[-2]
            print(v_time)
            if int(v_time) < 5 and type == 3:
                response = requests.get(url=url, headers=headers)
                res = response.text
                playurl = re.findall('"playurl":"(.*?)"', res, re.S)[0]
                playurl = playurl.replace('\\','')
                filename = download_video(playurl)

                #上传视频
                os_path = oss_video_pre(filename,1)
                #post 视频
                repeatid = hashlib.md5()
                repeatid.update(url.encode('utf-8'))
                repeatid = repeatid.hexdigest()
                print(repeatid)
                tagId = 3
                res_video = video_send(title, os_path, repeatid, tagId,i)
                if res_video:
                    update_haokan_video_flag(url)
                os.remove(video_filePath + filename)
            elif 5 <= int(v_time) < 20 and type == 3:
                response = requests.get(url=url, headers=headers)
                res = response.text
                playurl = re.findall('"playurl":"(.*?)"', res, re.S)[0]
                playurl = playurl.replace('\\','')
                filename = download_video(playurl)

                #上传视频
                os_path = oss_video_pre(filename,1)
                #post 视频
                repeatid = hashlib.md5()
                repeatid.update(url.encode('utf-8'))
                repeatid = repeatid.hexdigest()
                print(repeatid)
                tagId = 9
                res_video = video_send(title, os_path, repeatid, tagId,i)
                if res_video:
                    update_haokan_video_flag(url)
                os.remove(video_filePath + filename)