#!coding:utf-8
import match
import picture

import xstb
#new一个对象
xs = xstb.xstbMatcher("url")
#名称
site2 = 'xstb'
#将matcher注册到match中
match.register(site2,xs)
#调用runx()函数爬取对应的网页内容，并保存到TXT文件中 (遍历下一页直至尽头)
match.runx(site2)
# 根据指定的页数pages，爬取页面
# match.run(site2,pages)

#根据爬取的内容分词，并作图
picture.drawpicByTxt(site2)