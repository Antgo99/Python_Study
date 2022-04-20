# -*- coding = utf-8 -*-
# @Time : 2022/4/18 21:35
# @Author : Antgo99
# @File : testBs4.py
# @Software : PyCharm
import re

from bs4 import BeautifulSoup

file = open("./baidu.html","rb")

html = file.read()

bs = BeautifulSoup(html,"html.parser")

# print(bs.title)
# print(bs.body)
print(type(bs.title))

#1.Tag 标签及其内容 拿到的第一条内容

print(type(bs.title.string))

#2.NavigableString 标签里的内容（字符串）

print(type(bs))

#3.BeautifulSoup 表示整个文档

print(type(bs.a.string))

#4.一种特殊的NavigableString的字符串，输出的内容不包括注释符号

#文档的遍历
# print(bs.head.contents)

#文档的搜索
#1.find_all

#2.kwargs   参数

#3.text 参数

t_list = bs.find_all(text = re.compile("\d"))   #正则表达式
for item in t_list:
    print(item)
#4.limit

#5.css选择器
# t_list = bs.select('title') #通过标签来查找
# t_list = bs.select(".mnav") #通过类名来查找
# t_list = bs.select("#u1") #通过id来查找
# t_list = bs.select("a[class='bri']") #通过属性来查找
# t_list = bs.select("head > title")  #通过子标签来查找
