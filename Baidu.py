#!/usr/bin/env python
# encoding: utf-8

# Baidu.py
# HHSpider

# Created by Charles.Qiu on 2017/1/3 下午3:54.
# Copyright © 2017年 Charles.Qiu. All rights reserved.
# HomePage: https://github.com/CharlesQiu
# Email: qhs@outlook.com


import urllib2

response = urllib2.urlopen("http://www.baidu.com")
print response.read()