import smtplib
import random
from email.mime.text import MIMEText
from email.header import Header
import server_mysql
import hashlib

def random_pd():
    b = ''
    for j in range(8):
        a = str(random.randint(1, 9))
        b = b + a

    return b




def mail(b, recv):
    # 第三方 SMTP 服务b
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "daihw1212@qq.com"  # 用户名
    mail_pass = "rehznxmrhcdpdeja"  # 口令

    sender = 'daihw1212@qq.com'
    receivers = [recv, ]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText(b, 'plain', 'utf-8')
    message['From'] = Header("OO官方邮件", 'utf-8')
    message['To'] = Header(recv, 'utf-8')

    subject = '邮箱验证'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        print("准备发送文件")
        smtpObj = smtplib.SMTP_SSL(mail_host)
        print("住在连接服务器")
        smtpObj.connect(mail_host, 465)  # 25 为 SMTP 端口号
        print("正在登录服务器")
        smtpObj.login(mail_user, mail_pass)
        print("正在发送邮件")
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("发送成功")
        return 0
    except smtplib.SMTPException as mistake:
        print("发送失败",mistake)
        return 1

def main(recv):
    b = random_pd()
    mail(b, recv)
    server_mysql.insert_code(recv,b)
    print(1)