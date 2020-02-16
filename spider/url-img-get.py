#!/usr/bin/python
import os
import re
from urllib import request  #从urllib包中导入request模块
import chardet #导入chardet模块进行检测编码类型

def getHtml(url):
    page = request.urlopen(url)
    html = page.read()
    #自动检测网页编码格式，然后以相应的编码格式解码出来，如果没有检测到，则使用默认的设置格式
    ct = chardet.detect(html)
    return html.decode(ct.get("encoding","utf-8"))

def getImage(html):
    reg = r'"thumbURL":"(https.*?.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        request.urlretrieve(imgurl,"C:/Users/jorh/Desktop/python-execise/data/%d.jpg"%x)
        print("x = %d"%x)
        x += 1
        if x > 5:
            break
    return imglist
html = getHtml("https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%D7%C0%C3%E6&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111")
fo = open('C:/Users/jorh/Desktop/python-execise/data/test.txt','w',encoding = "utf - 8")
#print(fo.name)
fo.write(html)
fo.close()
fr = open('C:/Users/jorh/Desktop/python-execise/data/test.txt')
str1 = fr.readline()
print('str1 is:',str1)
fr.close()

path = os.path.dirname('test.txt')
print('the path is:',path)
#print(html)
print(getImage(html))
#getImage(html)










