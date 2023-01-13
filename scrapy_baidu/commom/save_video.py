import pymysql, datetime
# ---------连接--------------
connect = pymysql.connect(host='localhost',   # 本地数据库
                          user='root',
                          password='123456',
                          db='news_db',
                          charset='utf8') #服务器名,账户,密码，数据库名称
cur = connect.cursor()

# 通过cursor执行增删查改

# def save_xigua(title, href, target, video_time, type=3):
#     #去重并修改数据库
#     try:
#         now = datetime.datetime.now()
#         now = now.strftime("%Y-%m-%d %H:%M:%S")
#         check_url = """
#         select href from xigua_video where href = "%s" """ % href
#         # print('check_url',check_url)
#         cur.execute(check_url)
#         fetch = cur.fetchall()
#         # print(fetch)
#         if not fetch:
#             ss = """insert into xigua_video(title, href, target, create_time, video_time, type)
#                         value ("%s", "%s", "%s", "%s", "%s", "%s")""" %(title, href, target, now, video_time, type)
#             cur.execute(ss)
#             # 提交sql语句
#             connect.commit()
#
#     except Exception as error:
#         # 出现错误时打印错误日志
#         print(error)


def read_item():
    #读取数据库
    # select * from xigua_video where flag = FALSE  and href is not null and  video_time < 5  limit 100"""
    try:
        read_url = """
        select * from xigua_video where href  is not null and flag = 0  order by create_time desc """
        cur.execute(read_url)
        fetch = cur.fetchall()
        return fetch

    except Exception as error:
        # 出现错误时打印错误日志
        print(error)


# def read_xigua_videos_item():
#     #读取数据库
#     # select * from xigua_video where flag = FALSE  and href is not null and  video_time < 5  limit 100"""
#     try:
#         read_url = """
#         select * from xigua_video where href is not null and flag = 0 and type = 9 and video_time like '%视频%'"""
#         cur.execute(read_url)
#         fetch = cur.fetchall()
#         return fetch
#
#     except Exception as error:
#         # 出现错误时打印错误日志
#         print(error)

# def save_weibo(title, type, mid,source_src):
#     try:
#         now = datetime.datetime.now()
#         now = now.strftime("%Y-%m-%d %H:%M:%S")
#
#         ss = """insert into toutiao_news(title, type, create_time,mid,source_src,flag )
#                         value ("%s", "%s", "%s", "%s", "%s", 1)""" %(title, type, now,mid,source_src )
#         cur.execute(ss)
#         # 提交sql语句
#         connect.commit()
#
#     except Exception as error:
#     # 出现错误时打印错误日志
#         print(error)


def save_haokan(title, href, target, video_time, type=3):
    #去重并修改数据库
    try:
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        check_url = """
        select href from xigua_video where haokan_url = "%s" """ % href
        # print('check_url',check_url)
        cur.execute(check_url)
        fetch = cur.fetchall()
        # print(fetch)
        if not fetch:
            ss = """insert into xigua_video(title, haokan_url, target, create_time, video_time, type)
                        value ("%s", "%s", "%s", "%s", "%s", "%s")""" %(title, href, target, now, video_time, type)
            cur.execute(ss)
            # 提交sql语句
            connect.commit()

    except Exception as error:
        # 出现错误时打印错误日志
        print(error)

def read_haokan_item():
    #读取数据库
    try:
        read_url = """
        select * from xigua_video where flag = FALSE  and haokan_url is not null"""
        cur.execute(read_url)
        fetch = cur.fetchall()
        return fetch

    except Exception as error:
        # 出现错误时打印错误日志
        print(error)


def read_b_item():
    #读取数据库
    try:
        read_url = """
        select * from xigua_video where flag = FALSE  and b_url is not null"""
        cur.execute(read_url)
        fetch = cur.fetchall()
        return fetch

    except Exception as error:
        # 出现错误时打印错误日志
        print(error)



# def save_b_url(title, href, target, video_time, type=9):
#     #去重并修改数据库
#     try:
#         now = datetime.datetime.now()
#         now = now.strftime("%Y-%m-%d %H:%M:%S")
#         check_url = """
#         select href from xigua_video where b_url = "%s" """ % href
#         # print('check_url',check_url)
#         cur.execute(check_url)
#         fetch = cur.fetchall()
#         # print(fetch)
#         if not fetch:
#             ss = """insert into xigua_video(title, b_url, target, create_time, video_time, type)
#                         value ("%s", "%s", "%s", "%s", "%s", "%s")""" %(title, href, target, now, video_time, type)
#             cur.execute(ss)
#             # 提交sql语句
#             connect.commit()
#
#     except Exception as error:
#         # 出现错误时打印错误日志
#         print(error)


def save_tengxun(title, href, target, video_time, type=9):
    #去重并修改数据库
    try:
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        check_url = """
        select tengxun_url from xigua_video where tengxun_url = "%s" """ % href
        # print('check_url',check_url)
        cur.execute(check_url)
        fetch = cur.fetchall()
        # print(fetch)
        if not fetch:
            ss = """insert into xigua_video(title, tengxun_url, target, create_time, video_time, type)
                        value ("%s", "%s", "%s", "%s", "%s", "%s")""" %(title, href, target, now, video_time, type)
            cur.execute(ss)
            # 提交sql语句
            connect.commit()

    except Exception as error:
        # 出现错误时打印错误日志
        print(error)

def read_tengxun_item():
    #读取数据库
    try:
        read_url = """
        select * from xigua_video where flag = FALSE  and tengxun_url is not null"""
        cur.execute(read_url)
        fetch = cur.fetchall()
        return fetch

    except Exception as error:
        # 出现错误时打印错误日志
        print(error)