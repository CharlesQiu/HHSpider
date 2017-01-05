#!/usr/bin/env python
# encoding: utf-8

# Regular.py
# HHSpider

# Created by Charles.Qiu on 2017/1/4 下午3:25.
# Copyright © 2017年 Charles.Qiu. All rights reserved.
# HomePage: https://github.com/CharlesQiu
# Email: qhs@outlook.com

import re

# 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
pattern = re.compile(r'hello')

# 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, 'helloo CQC!')
result3 = re.match(pattern, 'helo CQC!')
result4 = re.match(pattern, 'hello CQC!')

if result1:
    print result1.group()
else:
    print 'result1匹配失败'

if result2:
    print result2.group()
else:
    print 'result2匹配失败'

if result3:
    print result3.group()
else:
    print 'result3匹配失败'

if result4:
    print result4.group()
else:
    print 'result4匹配失败'

# 匹配如下内容：单词+空格+单词+任意字符
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')

print "m.string:", m.string
print "m.re:", m.re
print "m.pos:", m.pos
print "m.endpos:", m.endpos
print "m.lastindex:", m.lastindex
print "m.lastgroup:", m.lastgroup
print "m.group():", m.group()
print "m.group(1,2):", m.group(1, 2)
print "m.groups():", m.groups()
print "m.groupdict():", m.groupdict()
print "m.start(2):", m.start(2)
print "m.end(2):", m.end(2)
print "m.span(2):", m.span(2)
print r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3')

pattern_split = re.compile(r'\d+')
print re.split(pattern_split,'one1two2three3four4')
print re.findall(pattern_split, 'one1two2three3four4')
for m in re.finditer(pattern_split,'one1two2three3four4'):
    print m.group(),

pattern_subn = re.compile(r'(\w+) (\w+)')
print pattern_subn.subn(r'\2 \1', 'i say, hello world!')

def fun(m):
    return m.group(1).title() + ' ' + m.group(2).title()

print pattern_subn.subn(fun, 'i say, hello world!')