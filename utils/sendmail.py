import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

class SendMail:
    def __init__(self):
        self.sender_email = "aaaaaaaa@qq.com"
        self.user_list = ["aaaaaa@163.com","bbbbbbb@163.com"]
        self.host = "smtp.qq.com"
        self.user = "Tom"
        self.pwd = "wereacgcsdowcaha"
        self.message = "This is test email!"
        self.mail_title = "Testing E-mail"
	#群发邮件
    def send_group_mail(self):
        user = "Eric" + "<" + self.sender_email + ">"
        msg = MIMEText(self.message,_subtype='plain',_charset='utf-8')
        msg['Subject'] = self.mail_title
        msg['From'] = self.sender_email
        msg['To'] = ";".join(self.user_list)
        server = smtplib.SMTP()
        server.connect(self.host)
        server.login(self.sender_email,self.pwd)
        server.sendmail(user,self.user_list,msg.as_string())
        server.close()
        print("邮件发送成功！")