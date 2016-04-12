#!/bin/env python3
#coding=utf-8

import time,datetime

x = 5

now_str = datetime.datetime.now().strftime("%s")
now_array = time.localtime(float(now_str))
#now_human = time.strftime("%Y%m%d %H:%M:%S",now_array)
now_human = time.strftime("%Y%m%d %Y-%M-%D",now_array)
xminutes_ago_human = (datetime.datetime.now()-datetime.timedelta(minutes=int(x))).strftime("%Y%m%d %H:%M:%S")
xminutes_ago_str = (datetime.datetime.now()-datetime.timedelta(minutes=int(x))).strftime("%s")




print ("now_str=",now_str)
print ("now_array=",now_array)
print ("now_human=",now_human)

print ("xminutes_ago_human=",xminutes_ago_human)
print ("xminutes_ago_str=",xminutes_ago_str)
