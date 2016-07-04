#!/bin/env python3
# coding=utf-8
# Filename    : 0001.py
# Date        : 2016-03-02 10:12:37
# Author      : statby
# Description : v1

import string
import random

letters = string.ascii_letters
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digit = string.digits
hexadecimal = string.hexdigits    #16进制
punctuation = string.punctuation  #特殊符号
whitespace = string.whitespace    #制表符、换行等
printable = string.printable      #数字+大小写+特殊符号+换行等
default_type = string.ascii_letters + string.digits + string.punctuation

all_code=[]
def get_string(length,num,type=default_type):
    for nums in range(num):
        code=''
        for lengths in range(length):
            code+=random.choice(type)
        all_code.append(code)
    return (all_code)

def print_pwd(length,num,type=default_type):
    for i in get_string(length,num,type=default_type):
        print (i)

if __name__ == '__main__':
    print_pwd(16,20)
