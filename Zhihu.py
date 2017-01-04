#!/usr/bin/env python
# encoding: utf-8

# Zhihu.py
# HHSpider

# Created by Charles.Qiu on 2017/1/3 下午4:08.
# Copyright © 2017年 Charles.Qiu. All rights reserved.
# HomePage: https://github.com/CharlesQiu
# Email: qhs@outlook.com

import urllib2

# response = urllib2.urlopen("http://www.zhihu.com")
# print response.read()

# requset = urllib2.Request('http://www.xxxxx.com', timeout=10)
# try:
#     response = urllib2.urlopen('http://www.xxxxx.com', timeout=3)
#     print response.read()
# except urllib2.URLError, e:
#     print e.reason

import urllib2

req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req)
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
else:
    print "OK"