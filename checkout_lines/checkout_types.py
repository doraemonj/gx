import pymysql, datetime
# ---------连接--------------
connect = pymysql.connect(host='localhost',   # 本地数据库
                          user='root',
                          password='123456',
                          db='news_db',
                          charset='utf8') #服务器名,账户,密码，数据库名称
cur = connect.cursor()

read_url = """
select case
    when type = 1
    then '热点' 
    when type = 2 
    then '时尚' 
    when type = 3
    then '星座'
    when type = 4 
    then '情感'
    when type = 5
    then '娱乐'
    when type = 6
    then '游戏'
    when type = 9 
    then '国际'
    when type = 21 
    then '军事' 
    when type = 23
    then '美食' 
    when type = 22 
    then '健康' 
    when type = 18 
    then '财经' 
    when type = 17 
    then '科技' 
    when type = 16 
    then '旅游' 
    when type = 24 
    then '汽车' 
    when type = 10 
    then '动漫' 
    when type = 19 
    then '种草' 
    when type = 25 
    then '美女' 
    when type = 26 
    then '帅哥' 
    when type = 11 
    then '论坛' 
    when type = 20 
    then '体育' 
    end as idstatus,
    count(*) from toutiao_news  where   create_time >  '2022-11-28 12:00:00' group by type  """
cur.execute(read_url)
fetch = cur.fetchall()

print(fetch)


read_url = """
select 
    case
    when type = 1
    then '热点' 
    when type = 2 
    then '时尚' 
    when type = 3
    then '星座'
    when type = 4 
    then '情感'
    when type = 5
    then '娱乐'
    when type = 6
    then '游戏'
    when type = 9 
    then '国际'
    when type = 21 
    then '军事' 
    when type = 23
    then '美食' 
    when type = 22 
    then '健康' 
    when type = 18 
    then '财经' 
    when type = 17 
    then '科技' 
    when type = 16 
    then '旅游' 
    when type = 24 
    then '汽车' 
    when type = 10 
    then '动漫' 
    when type = 19 
    then '种草' 
    when type = 25 
    then '美女' 
    when type = 26 
    then '帅哥' 
    when type = 11 
    then '论坛' 
    when type = 20 
    then '体育'
  end as idstatus,count(*)
  from toutiao_news  where  flag = TRUE and create_time >  '2022-11-28 12:00:00' group by type  """
cur.execute(read_url)
fetch = cur.fetchall()

print(fetch)


# read_url = """
# select count(*) from xigua_video where flag = 1 and create_time > '2022-11-24 12:00:00'
# """
# cur.execute(read_url)
# fetch = cur.fetchall()
#
# print(fetch)
