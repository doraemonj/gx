import pymysql, datetime
# ---------连接--------------
connect = pymysql.connect(host='localhost',   # 本地数据库
                          user='root',
                          password='12345678',
                          db='test1',
                          charset='utf8') #服务器名,账户,密码，数据库名称
cur = connect.cursor()

# 通过cursor执行增删查改


def process_item(url, title, type):
    #去重并修改数据库
    try:
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        check_url = """
        select url from toutiao_news where url = "%s" """ % url
        # print('check_url',check_url)
        cur.execute(check_url)
        fetch = cur.fetchall()
        # print(fetch)
        if not fetch:
            ss = """insert into toutiao_news(url, title, type, create_time)
                        value ("%s", "%s", "%s", "%s")""" %(url, title , type, now)
            cur.execute(ss)
            # 提交sql语句
            connect.commit()


    except Exception as error:
        # 出现错误时打印错误日志
        print(error)

def read_item(type):
    #读取数据库
    try:
        read_url = """
        select * from toutiao_news where type = %s and flag = FALSE """ % type
        cur.execute(read_url)
        fetch = cur.fetchall()
        return fetch

    except Exception as error:
        # 出现错误时打印错误日志
        print(error)


def read_all_item():
    #读取数据库         # select * from toutiao_news where flag = FALSE """
    try:
        read_url = """
        select * from toutiao_news where flag = FALSE and url is not null"""
        cur.execute(read_url)
        fetch = cur.fetchall()
        return fetch

    except Exception as error:
        # 出现错误时打印错误日志
        print(error)


def read_detail_item(type):
    #读取数据库         # select * from toutiao_news where flag = FALSE """
    try:
        read_url = """
        select * from toutiao_news where flag = FALSE and url is not null and type = %s order by create_time desc limit  100""" %type
        cur.execute(read_url)
        fetch = cur.fetchall()
        return fetch

    except Exception as error:
        # 出现错误时打印错误日志
        print(error)


def update_flag(url, contentAttr, source_ele):
    #去重并修改数据库
    try:
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        check_url = """
        select url from toutiao_news where url = "%s" """ % url
        # print('check_url',check_url)
        cur.execute(check_url)
        fetch = cur.fetchall()
        # print(fetch)
        if fetch:
            # ss = """update toutiao_news set flag = True and contentAttr = "%s" where url = "%s" """ \
            #      %(contentAttr, url)
            ss = """update toutiao_news set flag = True, source_src = "%s" where url = "%s" """ \
                 %(source_ele, url)
            # print(ss)
            cur.execute(ss)
            # 提交sql语句
            connect.commit()
    except Exception as error:
        # 出现错误时打印错误日志
        print(error)

def update_errflag(url):
    #去重并修改数据库
    try:
        check_url = """
        select url from toutiao_news where url = "%s" """ % url
        # print('check_url',check_url)
        cur.execute(check_url)
        fetch = cur.fetchall()
        # print(fetch)
        if fetch:
            ss = """update toutiao_news set flag = True, errflg = 1 where url = "%s" """ \
                 %(url)
            # print(ss)
            cur.execute(ss)
            # 提交sql语句
            connect.commit()
    except Exception as error:
        # 出现错误时打印错误日志
        print(error)


def create_src_item(url, oss_url, type):
    #去重并修改数据库 ossurl
    try:
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        check_url = """
        select url from src_detail where url = "%s" """ % url
        # print('check_url',check_url)
        cur.execute(check_url)
        fetch = cur.fetchall()
        # print(fetch)
        if not fetch:
            ss = """insert into src_detail(url, oss_url, type, create_time)
                        value ("%s", "%s", "%s", "%s")""" %(url, oss_url , type, now)
            cur.execute(ss)
            # 提交sql语句
            connect.commit()
    except Exception as e:
        print(e)


# def update_video_flag(href):
#     #修改数据库
#     try:
#         check_url = """
#         select href from xigua_video where href = "%s" """ % href
#         # print('check_url',check_url)
#         cur.execute(check_url)
#         fetch = cur.fetchall()
#         # print(fetch)
#         if fetch:
#             # ss = """update toutiao_news set flag = True and contentAttr = "%s" where url = "%s" """ \
#             #      %(contentAttr, url)
#             ss = """update xigua_video set flag = True where href = "%s" """ \
#                  %(href,)
#             # print(ss)
#             cur.execute(ss)
#             # 提交sql语句
#             connect.commit()
#     except Exception as error:
#         # 出现错误时打印错误日志
#         print(error)

def insert_update_video_flag(title, repeatid, tagId ,os_path):
    # print('title',title)
    #去重并修改数据库 ossurl
    try:
        check_url = """
        select repeatid from src_detail where repeatid = "%s" """ % repeatid
        # print('check_url',check_url)
        cur.execute(check_url)
        fetch = cur.fetchall()
        # print(fetch)
        if not fetch:
            ss = """insert into src_detail(title, oss_url, type, repeatid)
                        value ("%s", "%s", "%s", "%s")""" %(title, os_path , tagId, repeatid)
            cur.execute(ss)
            # 提交sql语句
            connect.commit()
    except Exception as e:
        print(e)


# def update_errflag(href):
#     #去重并修改数据库
#     try:
#         check_url = """
#         select url from toutiao_news where url = "%s" """ % href
#         # print('check_url',check_url)
#         cur.execute(check_url)
#         fetch = cur.fetchall()
#         # print(fetch)
#         if fetch:
#             ss = """update toutiao_news set flag = True, errflg = 1 where url = "%s" """ \
#                  %(href,)
#             # print(ss)
#             cur.execute(ss)
#             # 提交sql语句
#             connect.commit()
#     except Exception as error:
#         # 出现错误时打印错误日志
#         print(error)


def update_wberrflag(mid):
    #去重并修改数据库
    try:
        check_url = """
        select href from xigua_video where mid = "%s" """ % mid
        # print('check_url',check_url)
        cur.execute(check_url)
        fetch = cur.fetchall()
        # print(fetch)
        if fetch:
            ss = """update xigua_video set flag = True, errflg = 1 where href = "%s" """ \
                 %(mid,)
            # print(ss)
            cur.execute(ss)
            # 提交sql语句
            connect.commit()
    except Exception as error:
        # 出现错误时打印错误日志
        print(error)


def save_car_item(url, title, type, source_src):
    #去重并修改数据库
    try:
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")

        ss = """insert into toutiao_news(url,title, type, create_time,source_src)
                    value ("%s", "%s", "%s", "%s", "%s")""" %(url, title, type, now, source_src)
        cur.execute(ss)
        # 提交sql语句
        connect.commit()


    except Exception as error:
        # 出现错误时打印错误日志
        print(error)


def read_car_item():
    #读取数据库         # select * from toutiao_news where flag = FALSE """
    try:
        read_url = """
        select title from toutiao_news where flag = FALSE and type = 24 """
        cur.execute(read_url)
        fetch = cur.fetchall()
        return fetch

    except Exception as error:
        # 出现错误时打印错误日志
        print(error)

def update_haokan_video_flag(href):
    #修改数据库
    try:
        check_url = """
        select href from xigua_video where haokan_url = "%s" """ % href
        # print('check_url',check_url)
        cur.execute(check_url)
        fetch = cur.fetchall()
        # print(fetch)
        if fetch:
            # ss = """update toutiao_news set flag = True and contentAttr = "%s" where url = "%s" """ \
            #      %(contentAttr, url)
            ss = """update xigua_video set flag = True where haokan_url = "%s" """ \
                 %(href,)
            # print(ss)
            cur.execute(ss)
            # 提交sql语句
            connect.commit()
    except Exception as error:
        # 出现错误时打印错误日志
        print(error)


def update_b_video_flag(href):
    #修改数据库
    try:
        check_url = """
        select href from xigua_video where b_url = "%s" """ % href
        # print('check_url',check_url)
        cur.execute(check_url)
        fetch = cur.fetchall()
        # print(fetch)
        if fetch:
            # ss = """update toutiao_news set flag = True and contentAttr = "%s" where url = "%s" """ \
            #      %(contentAttr, url)
            ss = """update xigua_video set flag = True where b_url = "%s" """ \
                 %(href,)
            # print(ss)
            cur.execute(ss)
            # 提交sql语句
            connect.commit()
    except Exception as error:
        # 出现错误时打印错误日志
        print(error)