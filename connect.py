# 导入mysql模块
import mysql.connector

# 连接数据库
conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = '12345678',
                       db = 'test1',
                       charset = 'utf8mb4',
                       cursorclass = pymysql.cursors.DictCursor)
cur = conn.cursor()

# 创建数据库
cur.execute('''CREATE TABLE student (
    id INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    age INT(10) NOT NULL
 )''')

# 插入数据
cur.execute("INSERT INTO student(name, age) VALUES ('张三', 25)")
cur.execute("INSERT INTO student(name, age) VALUES ('李四', 30)")
cur.execute("INSERT INTO student(name, age) VALUES ('王五', 28)")

# 提交事务
conn.commit()

# 关闭连接
cur.close()
conn.close()