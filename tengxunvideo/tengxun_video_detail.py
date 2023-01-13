import requests, re
from tqdm import tqdm

# url = 'https://vd.l.qq.com/proxyhttp'
url = 'https://vd.l.qq.com/proxyhttp'


# data = {"buid":"vinfoad","vinfoparam":"charge=0&otype=ojson&defnpayver=3&spau=1&spaudio=0&spwm=1&sphls=2&host=v.qq.com&refer=https%3A%2F%2Fv.qq.com%2Fx%2Fpage%2Fs3357z9goyo.html&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fpage%2Fs3357z9goyo.html&sphttps=1&encryptVer=8.1&cKey=1E77B1A78C6B360E5D67C74AD5F674F1033A98190DA90C637B889C89943AD76C2B988BFF8C2C7CFB284F957EF71CCE01239DE7DC021E81166A35BBE82172A3EDC5D36027169FF38A15C69DB2B12662E31CAB3771C1E31617D2FC92C16E386F3D9F60EB71CAD2F731439B53139FD48324CCA9039C86FBD6E244CDB0F97BB5588AFB91DFAA3C123E6124748BF17FC0FCB411AA1573A4E3CFD75C396A2BBACFF99CD0F4CA3C18531F4E3C7FA21FE7013544CF8158F08F04A25CB0C4144D5E5C3C5FC04C4F1C49DB888998851A3BD8091F43&clip=4&guid=0ccdb2e470bfe8e2&flowid=542a3076084c930e9280117646b2203e&platform=10201&sdtfrom=v1010&appVer=3.5.57&unid=&auth_from=&auth_ext=&vid=s3357z9goyo&defn=&fhdswitch=0&dtype=3&spsrt=2&tm=1668931398&lang_code=0&logintoken=%7B%22access_token%22%3A%226B4E185EF2F768A1C6B69383C12F09DE%22%2C%22appid%22%3A%22101483052%22%2C%22vusession%22%3A%22gbFS-4eySGA050z0byYStA.N%22%2C%22openid%22%3A%22DFAD55CF8540D591F4A17190839FC3EC%22%2C%22vuserid%22%3A%22169789336%22%2C%22video_guid%22%3A%220ccdb2e470bfe8e2%22%2C%22main_login%22%3A%22qq%22%7D&spvvpay=1&spadseg=3&spav1=15&hevclv=28&spsfrhdr=0&spvideo=0&spm3u8tag=67&spmasterm3u8=3&drm=40","sspAdParam":"{\"ad_scene\":1,\"pre_ad_params\":{\"ad_scene\":1,\"user_type\":1,\"video\":{\"base\":{\"vid\":\"s3357z9goyo\",\"cid\":\"\"},\"is_live\":false,\"type_id\":1,\"referer\":\"\",\"url\":\"https://v.qq.com/x/page/s3357z9goyo.html\",\"flow_id\":\"542a3076084c930e9280117646b2203e\",\"refresh_id\":\"a1947e58ea9f6ad477f56803101d710c_1668917048\"},\"platform\":{\"guid\":\"0ccdb2e470bfe8e2\",\"channel_id\":0,\"site\":\"web\",\"platform\":\"in\",\"from\":0,\"device\":\"pc\",\"play_platform\":10201,\"pv_tag\":\"www_baidu_com\"},\"player\":{\"version\":\"1.12.2\",\"plugin\":\"1.15.12\",\"switch\":1,\"play_type\":\"0\",\"img_type\":\"webp\"},\"token\":{\"type\":1,\"vuid\":169789336,\"vuser_session\":\"gbFS-4eySGA050z0byYStA.N\",\"app_id\":\"101483052\",\"open_id\":\"DFAD55CF8540D591F4A17190839FC3EC\",\"access_token\":\"6B4E185EF2F768A1C6B69383C12F09DE\"}}}","adparam":"pf=in&pf_ex=pc&pu=1&pt=0&platform=10201&from=0&flowid=542a3076084c930e9280117646b2203e&guid=0ccdb2e470bfe8e2&coverid=&vid=s3357z9goyo&chid=0&tpid=1&refer=&url=https%3A%2F%2Fv.qq.com%2Fx%2Fpage%2Fs3357z9goyo.html&lt=qq&opid=DFAD55CF8540D591F4A17190839FC3EC&atkn=6B4E185EF2F768A1C6B69383C12F09DE&appid=101483052&uid=169789336&tkn=gbFS-4eySGA050z0byYStA.N&rfid=a1947e58ea9f6ad477f56803101d710c_1668917048&v=1.12.2&vptag=www_baidu_com&ad_type=LD%7CKB%7CPVL&live=0&appversion=3.2.22&ty=web&adaptor=1&dtype=1&resp_type=json&s_img=webp"}
data = {"buid":"vinfoad","vinfoparam":"charge=0&otype=ojson&defnpayver=3&spau=1&spaudio=0&spwm=1&sphls=2&host=v.qq.com&refer=https%3A%2F%2Fv.qq.com%2Fx%2Fpage%2Fs3357z9goyo.html&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fpage%2Fs3357z9goyo.html&sphttps=1&encryptVer=8.1&cKey=93C7C12EA1B8602EF12EB20C933240D342D39617357C37BF0D7539D68B6CBE57DB83EE09566037578D0E5FA7E02E2E455EB95569575DBC36528C9C8B189F61E67E787716207E4D4A015CE4CBA2A52A77EADAC756168577DE49B7176BBCC892F4F5262A5B89223D4FB999C164E5A4D9BEDD4B9AD7EA946143AFF0D3774FD58725480E22C03A04AF6CC46536976E87FAC08D599A9F35981ADD64014EDE44B60FC49E14B38D73684DA5A340F935D509A65ECC1AD32219C2515D56477A025088F5C8D316C98529E9E1E25A4A05E981752C90&clip=4&guid=0ccdb2e470bfe8e2&flowid=3e1347f3fad0c510c9af1ab264e32ba8&platform=10201&sdtfrom=v1010&appVer=3.5.57&unid=&auth_from=&auth_ext=&vid=s3357z9goyo&defn=&fhdswitch=0&dtype=3&spsrt=2&tm=1668933630&lang_code=0&logintoken=%7B%22access_token%22%3A%226B4E185EF2F768A1C6B69383C12F09DE%22%2C%22appid%22%3A%22101483052%22%2C%22vusession%22%3A%22DQvCYAeN22TxoXB6B1TRrg.N%22%2C%22openid%22%3A%22DFAD55CF8540D591F4A17190839FC3EC%22%2C%22vuserid%22%3A%22169789336%22%2C%22video_guid%22%3A%220ccdb2e470bfe8e2%22%2C%22main_login%22%3A%22qq%22%7D&spvvpay=1&spadseg=3&spav1=15&hevclv=28&spsfrhdr=0&spvideo=0&spm3u8tag=67&spmasterm3u8=3&drm=40","sspAdParam":"{\"ad_scene\":1,\"pre_ad_params\":{\"ad_scene\":1,\"user_type\":1,\"video\":{\"base\":{\"vid\":\"s3357z9goyo\",\"cid\":\"\"},\"is_live\":false,\"type_id\":1,\"referer\":\"\",\"url\":\"https://v.qq.com/x/page/s3357z9goyo.html\",\"flow_id\":\"3e1347f3fad0c510c9af1ab264e32ba8\",\"refresh_id\":\"5c718d64b582506953bfea1485123b6b_1668933397\"},\"platform\":{\"guid\":\"0ccdb2e470bfe8e2\",\"channel_id\":0,\"site\":\"web\",\"platform\":\"in\",\"from\":0,\"device\":\"pc\",\"play_platform\":10201,\"pv_tag\":\"www_baidu_com\"},\"player\":{\"version\":\"1.12.2\",\"plugin\":\"1.15.12\",\"switch\":1,\"play_type\":\"0\",\"img_type\":\"webp\"},\"token\":{\"type\":1,\"vuid\":169789336,\"vuser_session\":\"DQvCYAeN22TxoXB6B1TRrg.N\",\"app_id\":\"101483052\",\"open_id\":\"DFAD55CF8540D591F4A17190839FC3EC\",\"access_token\":\"6B4E185EF2F768A1C6B69383C12F09DE\"}}}","adparam":"pf=in&pf_ex=pc&pu=1&pt=0&platform=10201&from=0&flowid=3e1347f3fad0c510c9af1ab264e32ba8&guid=0ccdb2e470bfe8e2&coverid=&vid=s3357z9goyo&chid=0&tpid=1&refer=&url=https%3A%2F%2Fv.qq.com%2Fx%2Fpage%2Fs3357z9goyo.html&lt=qq&opid=DFAD55CF8540D591F4A17190839FC3EC&atkn=6B4E185EF2F768A1C6B69383C12F09DE&appid=101483052&uid=169789336&tkn=DQvCYAeN22TxoXB6B1TRrg.N&rfid=5c718d64b582506953bfea1485123b6b_1668933397&v=1.12.2&vptag=www_baidu_com&ad_type=LD%7CKB%7CPVL&live=0&appversion=3.2.22&ty=web&adaptor=1&dtype=1&resp_type=json&s_img=webp"}
header = {
'cookie': 'LPLFturn=301; LPVLturn=230; appuser=9439C45D19F0758D; o_minduid=nM8X3Nob_84g6HbqMpBIbOYg2YVvCA8x',
    'user-agent': 'PostmanRuntime/7.29.2',
}
json_data = requests.post(url=url, json=data, headers=header).json()
# print(json_data['vinfo'])
m3u8_url = re.findall('url":"(.*?)"', json_data['vinfo'])[3]
# print(m3u8_url)
m3u3_text = requests.get(m3u8_url).text
ts_list = re.sub('#E.*', '', m3u3_text).split()
for ts in tqdm(ts_list):
    ts_url = 'https://apd-4bdad9aa0f24994efe8344cee740cad1.v.smtcdns.com/omts.tc.qq.com/AdhJ5R6cexzrAz43lpoc7dngNnWWdNrdHGv8ra6_dQy0/B_ppPqCIXz9JbN8GvwkO8ikQ/svp_50069/mmdMREfHubA9DSH2mmG1SHDY_0IWwxAtIgkFwxh0KI1pC4fVyDNPrxiQqjWry1FBjm5Yuv8RehQGBO0dPY7t1N6sIoCZXR9gkVnBEQqpBS7JVH6CGqXhwKhQkTFZbd5eAK39GHCQ2ColpXE1XOFGfnX7oeKU7ld_IG9o7rW2GiI/' + ts
    # ts_url = 'https://apd-d84ed235f0e9197b96e5b4b8f0681028.v.smtcdns.com/omts.tc.qq.com/A59ybLKTRIVUlti8jC6ki4lBHT1SoOQd6qm8HRChAfaE/B_ppPqCIXz9JbN8GvwkO8ikQ/svp_50069/p4wW1shhfDgTlZsiOs5aheP_Tr34Q9220R5wn-1g8aItRgL6Ii8azNYMKsJeWRY0PD23Za59lCV9g6eB5gyWWqVyEag_TAan9apl2x_Z8CPvbHMi0pfPixi4AtB6thyPTojqpsF66_6ist2EjrKyaZpDlvpoT5R-ajZtFCpwmyI/' + ts
    ts_data = requests.get(ts_url).content
    with open('tengxun.mp4', mode='ab') as f:
        f.write(ts_data)