# -*- coding = utf-8 -*-
# @Time : 2022/4/18 20:21
# @Author : Antgo99
# @File : crawler_test.py
# @Software : PyCharm


from bs4 import BeautifulSoup  # 网页解析
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行sqlite数据库操作


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getdata(baseurl)
    # 3.保存数据
    savepath = ".\\豆瓣电影Top250.xls"
    # savedata(savepath)
    askURL(baseurl)


# 影片链接的规则
findLink = re.compile(r'<a href="(.*?)">')
# 影片的图片
findImg = re.compile(r'<img.*src="(.*?)"', re.S)
# 影片的片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片的评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 影片的评价人数
findJude = re.compile(r'<span>(\d*)人评价</span>')
# 影片的简介
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 影片的相关导演和演员
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 爬取网页
def getdata(baseurl):
    datalist = []
    for i in range(0, 1):
        url = baseurl + str(i * 25)  # 获取到每页的url
        html = askURL(url)  # 得到网页的源码
        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            data = []  # 保存一部电影的所有信息
            item = str(item)

            # 影片详情的链接
            link = re.findall(findLink, item)[0]  # re库用来通过正则表达式来查找指定的字符串
            print(link)

    return datalist


# 得到指定有个url网页的内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 100.0.4896.75 Safari / 537.36 Edg / 100.0.1185.39"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


# 保存数据
def savedata(savepath):
    print("save.....")


if __name__ == "__main__":
    main()
