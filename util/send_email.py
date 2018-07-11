import smtplib
from email.mime.text import MIMEText

class SendEmail:
    global send_user 
    global email_host 
    global password 
    send_user = 'xianjie_yang@loongjoy.com'
    email_host = 'smtp.exmail.qq.com'
    password = 'Yxj931227'
    def send_mail(self,user_list,sub,content):
        user = 'xianjie_yang@loongjoy.com' + '<' + send_user + '>'
        message = MIMEText(content,_subtype='plain',_charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ','.join(user_list)
        server = smtplib.SMTP_SSL()
        server.connect(email_host,465)
        server.login(send_user,password)
        server.sendmail(user,user_list,message.as_string())
        server.close()

if __name__ == '__main__':
    sen = SendEmail()
    user_list = ["1562007048@qq.com"]
    sub = '测试主题'
    content = '测试邮件内容'
    sen.send_mail(user_list,sub,content)
