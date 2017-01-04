#!/usr/bin/env python
# encoding: utf-8

# PlayGround.py
# HHSpider

# Created by Charles.Qiu on 2016/12/13 下午6:10.
# Copyright © 2016年 Charles.Qiu. All rights reserved.
# HomePage: https://github.com/CharlesQiu
# Email: qhs@outlook.com

# 教程：http://cuiqingcai.com/1052.html

import urllib2
import urllib

# request = urllib2.Request('http://www.baidu.com')
# response = urllib2.urlopen(request)
# print response.read()

values = {}
values['username'] = "10000@qq.com"
values['password'] = "xxxx"
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request_post = urllib2.Request(url, data)
resonse_post = urllib2.urlopen(request_post)
print resonse_post.read()