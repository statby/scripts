#!/bin/env python3
# coding=utf-8
# Date        : 2016-04-14 10:04:12
# Author      : Statby
# Description : 检查tengine concat 模块具体 某个url出错的脚本

import requests
import sys
import re

if len(sys.argv) != 2:
    print('Input concat url.')
    exit(1)

url = sys.argv[1]
cut = re.split('\?\?|\,',url)
single_url = [cut[0][:-1]+ str(i) for i in cut[1:]]

if not any(single_url):
    print('Wrong url!')
    exit(1)
#print(single_url)

def get_status(site):
    try:
        return True if requests.get(site).status_code == 200 else False
    except:
        print('wrong web site')
        exit(1)

def get_status_all():
    ok,err = [[] for i in range(2)]
    for i in single_url:
        if get_status(i):
            ok.append(i)
        else:
            err.append(i)
    if any(err):
        print('error!',err)
    else:
        print('all good!')

if __name__ == '__main__':
    get_status_all()
        


