#!/usr/bin/env python
# encoding: utf-8

# QiuBai.py
# HHSpider

# Created by Charles.Qiu on 2017/1/5 下午5:33.
# Copyright © 2017年 Charles.Qiu. All rights reserved.
# HomePage: https://github.com/CharlesQiu
# Email: qhs@outlook.com

# https://github.com/26huitailang/learn-sth-everyday/blob/master/practice/spider/qiushibaike.py#L23

class QiuBai:
	# 初始化方法，定义一些变量
	def __init__(self):
		self.pageIndex = 1
		self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
		self.headers = {'User-Agent': self.user_agent}
		self.stories = []
		self.enable = False

	# 开始方法
	def start(self):
		print u"正在读取糗事百科，回车查看新段子，q退出"
		self.enable = True  # 程序运行变量
		self.load_page()
		now_page = 0
		while self.enable:
			if len(self.stories) > 0:
				page_stories = self.stories.pop(0)
				now_page += 1

	def load_page(self):
		"""
		加载并提取页面的内容，加入到列表中
		:return:
		"""

		# 如未看页数少于2，则加载并抓取新一页补充
		if self.enable is True:
			if len(self.stories) < 2:

	def get_page(self, page_index):
		"""
		传入某一页面的索引后的页面代码
		:param pageIndex:
		:return:
		"""
		pass

	def get_page_items(self, page_index):
		"""
		传入某一页代码，返回本页不带图的段子列表
		:param pageIndex:
		:return:
		"""
		pass

	def get_one_story(self, page_stories, page):
		"""
		调用该方法，回车输出一个段子，q结束程序
		:param page_stories:
		:param page:
		:return:
		"""
		pass


if __name__ == '__main__':
	spider = QiuBai()
	spider.start()
