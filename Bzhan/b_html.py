from lazysdk import lazyrequests
from lazysdk import lazymd5
import fastmongo
import showlog

env_file_name_mongo = 'local.mongo.env'


def web_api_search(
        page: int = 1,
        page_size: int = 42,
        keyword: str = '欧美视频',
        search_type: str = 'video'
):
    qv_id = 'qf5vnWz2Jk1UCjWGeaFgW3lKOz27aKny'
    dynamic_offset = (page - 1) * 30
    url = 'https://api.bilibili.com/x/web-interface/search/type'
    params = {
        '__refresh__': True,
        '_extra': '',
        'context': '',
        'page': page,
        'page_size': page_size,
        'from_source': '',
        'from_spmid': 333.337,
        'platform': 'pc',
        'highlight': 1,
        'single_column': 0,
        'keyword': keyword,
        'qv_id': qv_id,
        'category_id': '',
        'search_type': search_type,
        'dynamic_offset': dynamic_offset
    }
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate",
        "accept-language": "zh-CN,zh;q=0.9",
        "origin": "https://search.bilibili.com",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        'cookie': "_uuid=1067A7661-ECB4-AD2E-710F1-C4AF4B3AAB6E24367infoc; buvid3=071E1FB9-4E9D-F675-FC73-EBF71502698928738infoc; b_nut=1665148026; buvid4=32D190EC-D94D-99F9-16FD-9ED757EF4D9028738-022100721-xWrW9RW0SscAM03ESt7jBw==; i-wanna-go-back=-1; nostalgia_conf=-1; rpdid=|(J|)R|~Y))k0J'uYYYk~kkRu; fingerprint=18e7f6cc53ea2a07151e4a1640a9ba47; buvid_fp_plain=undefined; DedeUserID=3461573018389263; DedeUserID__ckMd5=934ad58300c1a47f; buvid_fp=f602e0dc2c822f7ea8fea740ef2a42db; b_ut=5; bsource=search_baidu; CURRENT_QUALITY=0; blackside_state=1; SESSDATA=b0c65761,1683285604,341f7*b2; bili_jct=cc245489510dd1d757d16e3393e0dbd9; innersign=1; sid=5hv47ae6; PVID=1; CURRENT_FNVAL=4048; b_lsid=37A102AD8_184522D0648; bp_video_offset_3461573018389263=725735660862832800",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X -1_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    page_res = lazyrequests.lazy_requests(
        method='GET',
        url=url,
        params=params,
        headers=headers,
        return_json=True
    )
    """
    影响能不能返回的原因是cookie
    错误返回：{'code': -412, 'message': '请求被拦截', 'ttl': 1, 'data': None}
    正确返回：{'code': 0, 'message': '0', 'ttl': 1, 'data': {'seid'...}
    """
    code = page_res.get('code')
    if code == 0:
        page_data = page_res.get('data')
        num_pages = page_data.get('numPages')  # 总页数
        num_results = page_data.get('numResults')  # 总结果数
        result = page_data.get('result')  # 结果内容
        if result:
            for each_result in result:
                each_result['search_keyword'] = keyword  # 添加搜索参数
                each_result['gx_type_code'] = 9  # 添加光岘分类code
                each_result['gx_type_name'] = "欧美视频"  # 添加光岘分类名称
                each_result['arcurl_md5'] = lazymd5.md5_str(content=each_result['arcurl'])
            showlog.info(f'获取到 {len(result)} 条数据，正在存储...')
            fastmongo.safe_upsert(
                values=result,
                db='bilibili',
                collection='web_api_search',
                env_file_name=env_file_name_mongo,
                query_keys=['search_keyword', 'arcurl_md5']
            )
            showlog.info('存储完成')
            return True
        else:
            return False
    elif code == -412:
        showlog.warning(page_res)
        return False
    else:
        showlog.warning(page_res)
        return False


def get_search_all(
        keyword: str = '欧美视频',
        search_type: str = 'video'
):
    page = 1
    while True:
        showlog.info(f'正在采集第 {page} 页...')
        signal = web_api_search(
            page=page,
            keyword=keyword,
            search_type=search_type
        )
        if signal:
            page += 1
        else:
            break


if __name__ == '__main__':
    get_search_all()
