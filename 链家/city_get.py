

# -*- coding:utf-8 -*-
import csv
import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup

#我还不确定是哪一个URL 
url = "https://www.lianjia.com/city/"
# url ="https://www.lianjia.com"
#获取html页面
html=urlopen(url).read()
#获取BeatutifulSoup对象，用html5lib解析，html5lib v.s. lxml解析
#html5lib解析的容错性较好
bsobj=BeautifulSoup(html,"html5lib")
#得到 div class="city_list_section的div下所有a标签
# 在这个标签下，每个<a>标签下都对应着一条数据
city_tags=bsobj.find("div",{"class":"city_list_section"}).findChildren('a')
'''
    city_tags 内数据的格式如下：
    <a href="https://baotou.lianjia.com/">包头</a>

'''
#将每一条数据抽离，保存在citys.csv文件中
with open("./citys.csv","w")as f:
    writ=csv.writer(f)
    for city_tag in city_tags:
        city_url=city_tag.get("href")
        #太神奇了 我把后面的.encode("utf-8")问题就解决了 太神奇了太神奇了。。。
        city_name=city_tag.get_text()
        writ.writerow((city_name,city_url))
        print(city_name,city_url)


