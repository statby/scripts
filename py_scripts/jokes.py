#!/bin/env python3
# coding=utf-8
# Date        : 2016-04-12 15:56:54
# Author      : Statby
# Description : 

from urllib.request import urlopen
import smtplib
from email.mime.text import MIMEText

'''
import requests
def get_joke_content_request():
    joke_url = 'http://apix.sinaapp.com/joke/?appkey=trialuser'
    joke = requests.get(joke_url)
    content = joke.text[1:-16]
    return content
'''

def get_joke_content_urllib():
    joke_url = 'http://apix.sinaapp.com/joke/?appkey=trialuser'
    try:
        joke = urlopen(joke_url)
        joke_content = joke.read().decode('utf-8')[1:-16]
        return joke_content
    except:
        print('Get joke content error !')
        return False

mail_host="smtp.exmail.qq.com"
mail_user="admin@localhost.com"
mail_pass="pwd"
mail_postfix="localhost.com"
strTo = ['admin@localhost.com']

def send_mail(to_list, sub, content):
    address = mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = address
    msg['To'] = ','.join(strTo)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user, mail_pass)
        s.sendmail(address,  to_list, msg.as_string())
        s.close()
        return True
    except:
        print('send mail error')
        return False
if __name__ == '__main__':
        send_mail(strTo, 'joke', str(get_joke_content_urllib()))
