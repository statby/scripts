#!/bin/env python3 
#coding=utf-8
import requests
from bs4 import BeautifulSoup

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
}

weather = "http://www.weather.com.cn/weather1d/101280101.shtml"
gz_7= "http://www.weather.com.cn/weather/101280101.shtml"
sg_7 = "http://www.weather.com.cn/weather/101280201.shtml"
bj_7 = "http://www.weather.com.cn/weather/101010100.shtml"

r = requests.Session().get(gz_7,headers=header)

web_encoding = (r.encoding)
web_text = r.text
web_headers = (r.headers)
soup = BeautifulSoup(web_text,'html.parser')
f= (soup.prettify())

weather_now = soup.find(id='hidden_title')['value']
tabDays = soup.find_all(id="7d")

#print (web_headers)
#print (weather_now)

def print_weather(day):
  for days in range(1, day+1):
   day_list =  soup.find("li",attrs={"class":"dn","data-dn":"7d{0}".format(int(days))}).get_text().split("\n")
   while "" in day_list:
     day_list.remove("")
   for day_data in day_list:
     print (day_data,end=" ")
   print ()

#  1 >=day <=7
print_weather(7)
