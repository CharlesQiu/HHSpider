#!/usr/bin/env python
# encoding: utf-8

# BaiDuTieBa.py
# HHSpider

# Created by Charles.Qiu on 2017/1/6 下午5:17.
# Copyright © 2017年 Charles.Qiu. All rights reserved.
# HomePage: https://github.com/CharlesQiu
# Email: qhs@outlook.com

# http://tieba.baidu.com/p/4778121713
# http://cuiqingcai.com/993.html

import urllib2
import re

# 百度贴吧爬虫类
class BDTB:

    # 初始化，传入基地址，是否只看楼主的参数
    def __init__(self, seeLz):
        self.baseURL = 'http://tieba.baidu.com/p/4778121713'
        self.seeLZ = '?see_lz=' + str(seeLz)

    def getPage(self, pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"连接百度贴吧失败,错误原因", e.reason
                return None

    def getTitle(self, page):
        pattern = re.compile('<h3 class="core_title_txt.*?(.*?).*?</h3>', re.S)
        result = re.search(pattern, page)
        if result:
            print result.group(1)
        else:
            return None

    # # 开始方法
    # def start(self):
    #     pass


if __name__ == '__main__':
    tieba = BDTB(1)
    page = tieba.getPage(1)
    tieba.getTitle(page)

