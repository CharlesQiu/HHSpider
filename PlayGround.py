#!/usr/bin/env python
# encoding: utf-8

# PlayGround.py
# HHSpider

# Created by Charles.Qiu on 2016/12/13 下午6:10.
# Copyright © 2016年 Charles.Qiu. All rights reserved.
# HomePage: https://github.com/CharlesQiu
# Email: qhs@outlook.com

import urllib2

response = urllib2.urlopen('http://www.baidu.com')
print response.read()