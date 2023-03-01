import pymysql



#注册验证

def check_nick_name(nick_name):

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='mydb', charset='utf8')

    try:
        with conn.cursor() as cur:
            cur.execute("select nick_name from users where nick_name = '{}'".format(nick_name))
            rows = cur.fetchone()

    finally:
        conn.close()

    if rows:
        return 0     #用户名存在
    else:
        return 1     #用户名不存在



def check_user_name(user_name):

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='mydb', charset='utf8')

    try:
        with conn.cursor() as cur:
            cur.execute("select user_name from users where user_name = '{}'".format(user_name))
            rows = cur.fetchone()

    finally:
        conn.close()

    if rows:
        return 0  # 账号存在
    else:
        return 1  # 账号不存在


def check_email(email):

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='mydb', charset='utf8')

    try:
        with conn.cursor() as cur:
            cur.execute("select email from users where email = '{}'".format(email))
            rows = cur.fetchone()

    finally:
        conn.close()

    if rows:
        return 0  # 邮箱存在
    else:
        return 1  # 邮箱不存在



#登录验证


def check_password(user_name, password):


    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='mydb', charset='utf8')

    try:
        with conn.cursor() as cur:
            cur.execute("select passwd from users where user_name = '{}'".format(user_name))
            rows = cur.fetchone()

    finally:
        conn.close()

    if rows[0] == password:
        return 0  # 密码正确
    else:
        return 1  # 密码错误


#忘记密码
def check_code(email,ver_code):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='mydb', charset='utf8')

    try:
        with conn.cursor() as cur:
            cur.execute("select ver_code from ver_table where email = '{}'".format(email))
            rows = cur.fetchone()

    finally:
        conn.close()

    if rows[0] == ver_code:
        return 0  # 验证码正确
    else:
        return 1  # 验证码错误

def check_code_email(email):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='mydb', charset='utf8')

    try:
        with conn.cursor() as cur:
            cur.execute("select email from ver_table where email = '{}'".format(email))
            rows = cur.fetchone()

    finally:
        conn.close()
    if rows:
        return 1 # 邮箱存在
    else:
        return 0  # 邮箱不存在

def insert_code(email,the_code):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='mydb', charset='utf8')

    try:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO `mydb`.`ver_table` ( `email`, `ver_code` ) values ('{}', '{}')".format( email , the_code))
            conn.commit()
    finally:
        conn.close()

def delet_code(email):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='mydb', charset='utf8')

    try:
        with conn.cursor() as cur:
            cur.execute("delete from ver_table where email = '{}'".format(email))
            conn.commit()
    finally:
        conn.close()

def modify_pd(email, password):
    '''
    根据邮箱改密码
    :param email,password:
    :return:
    '''
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='mydb', charset='utf8')
    try:
        with conn.cursor() as cur:
            cur.execute("update users set passwd = '{}' where email = '{}'".format(password, email))
            conn.commit()
    finally:
        conn.close()



def update_passwd(user_name, news_passwd):
    '''
    修改密码
    :return:
    '''
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='mydb', charset='utf8')

    try:
        with conn.cursor() as cur:
            cur.execute("update users set passwd = '{}' where user_name = '{}'".format(news_passwd, user_name))
            conn.commit()
    finally:
        conn.close()



def add_user(information):
    '''
    添加用户
    :return:
    '''
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='mydb', charset='utf8')

    try:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO `mydb`.`users` (`nick_name`, `user_name`, `email`, `phone`, `passwd`) values ('{}', '{}', '{}', '{}', '{}')".format(information['nick_name'], information['user_name'] , information['email'] , information['phone'] , information['password']))
            conn.commit()
    finally:
        conn.close()


def select_user_name(email):
    '''
    根据用户名找昵称
    :param user_name:
    :return:
    '''
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='mydb', charset='utf8')

    try:
        with conn.cursor() as cur:
            cur.execute("select user_name from users where email = '{}'".format(email))
            rows = cur.fetchone()
    finally:
        conn.close()

    return rows[0]

def select_nick_name(user_name):
    '''
    根据用户名找昵称
    :param user_name:
    :return:
    '''
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='mydb', charset='utf8')

    try:
        with conn.cursor() as cur:
            cur.execute("select nick_name from users where user_name = '{}'".format(user_name))
            rows = cur.fetchone()
    finally:
        conn.close()

    return rows[0]




