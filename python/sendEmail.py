# -*- coding:utf-8 -*-
# Time : 2022/4/11 15:39 
# FileName : sendEmail.py
# Author : Gecko
# Description：发送邮件
import smtplib
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Config():
    fromaddr = '*@163.com'
    password = '*'
    smtpaddr = 'smtp.163.com'
    toaddrs = '*@qq.com'


def sendmail(subject, msg, Config):
    """
    @subject:邮件主题
    @msg:邮件内容
    @toaddrs:收信人的邮箱地址
    @fromaddr:发信人的邮箱地址
    @smtpaddr:smtp服务地址，可以在邮箱看，比如163邮箱为smtp.163.com
    @password:发信人的邮箱授权码, 而不是邮件的登陆密码
    """
    fromaddr = Config.fromaddr
    password = Config.password
    smtpaddr = Config.smtpaddr
    toaddrs = Config.toaddrs
    mail_msg = MIMEMultipart()
    mail_msg['Subject'] = subject
    mail_msg['From'] = fromaddr
    mail_msg['To'] = ','.join(toaddrs)
    mail_msg.attach(MIMEText(msg, 'html', 'utf-8'))
    from email.mime.application import MIMEApplication
    # zipFile = 'FiddlerRoot.zip'  # 附件上传
    # zipApart = MIMEApplication(open(zipFile, 'rb').read())
    # zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)
    # mail_msg.attach(zipApart)
    try:
        s = smtplib.SMTP()
        s.connect(smtpaddr)  # 连接smtp服务器
        s.login(fromaddr, password)  # 登录邮箱
        s.sendmail(fromaddr, toaddrs, mail_msg.as_string())  # 发送邮件
        s.quit()
        print("邮件发送成功！")
    except Exception as e:
        print("邮件发送失败！", e)
        print(traceback.format_exc())


if __name__ == '__main__':
    subject = '邮件主题'
    msg = '邮件内容'
    sendmail(subject, msg, Config())
