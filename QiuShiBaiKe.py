#!/usr/bin/env python
# encoding: utf-8

# QiuShiBaiKe.py
# HHSpider

# Created by Charles.Qiu on 2017/1/4 下午8:13.
# Copyright © 2017年 Charles.Qiu. All rights reserved.
# HomePage: https://github.com/CharlesQiu
# Email: qhs@outlook.com

import urllib
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

try:
	request = urllib2.Request(url, headers=headers)
	response = urllib2.urlopen(request)
	print response.read()
except urllib2.URLError, e:
	if hasattr(e, 'code'):
		print e.code
	if hasattr(e, 'reason'):
		print e.reason

content = response.read().decode('utf-8')
pattern = re.compile(
		'<div.*?author">.*?<img.*?>(.*?)</a>.*?<div.*?>' + 'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>')
