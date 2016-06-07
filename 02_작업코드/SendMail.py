# -*- coding: utf-8 -*-
"""
Created on Fri May 27 23:02:08 2016

@author: Ssenilen
"""

import smtplib
from email.mime.text import MIMEText

#gloval value
mailer = None

def SettingMailer():
    global mailer
    mailer= smtplib.SMTP("smtp.gmail.com", 587)
    mailer.ehlo()
    mailer.starttls()
    mailer.ehlo()
    mailer.login("pythonmailer2016@gmail.com", "1q2w3e4r1q2w3e4r")


def SendMailTest(mailaddress):
    text = "테스트 메일입니다."
    msg = MIMEText(text)
    senderAddr = "pythonmailer2016@gmail.com"
    recipientAddr = mailaddress
    
    msg['Subject'] = "테스트 메일"
    msg['From'] = senderAddr
    msg['To'] = recipientAddr
    
    global mailer
    mailer.sendmail(senderAddr, [recipientAddr], msg.as_string())
    mailer.close()
    print("메일 전송에 성공했습니다.")
    
def main():
    SettingMailer()
    mailaddress = input("결과를 전달받을 메일 주소를 입력해주세요: ")
    SendMailTest(mailaddress)
    
    