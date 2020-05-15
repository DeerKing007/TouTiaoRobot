import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def sendMail(title, Content):
    sender = '1005304721@qq.com'
    password = 'ltjuthwgtamobbie'   # 口令--->需要修改为授权码
    receivers = '16601348816@163.com'
    host = "smtp.qq.com"
    message = MIMEMultipart('related')
    subject = title
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receivers
    content = MIMEText(Content,'html','utf-8')
    message.attach(content)

    file=open("/Users/baidu/worker/TouTiaoRobot/accessory/logo.png", "rb")
    img_data = file.read()
    file.close()

    img = MIMEImage(img_data)
    img.add_header('Content-ID', 'imageid')
    message.attach(img)

    try:
        server=smtplib.SMTP_SSL(host, 465)
        server.login(sender, password)
        server.sendmail(sender, receivers, message.as_string())
        server.quit()
        print ("邮件发送成功")
    except smtplib.SMTPException as e:
        print(e)

if __name__ == '__main__':
    content='''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<img src="http://cms-bucket.nosdn.127.net/2018/12/10/7cc7ebe5f0ae4af3b1738f38a79405c8.jpg" alt="">
</body>
</html>
    '''
    sendMail('hello', content)
