import sys
import csv

from urllib.request import urlopen
from bs4 import BeautifulSoup
from house_info import house

def get_city_dict():
    city_dict={}
    with open("citys.csv","r") as f:
        reader=csv.reader(f)
        for city in reader:
            city_dict[city[0]]=city[1]
    return city_dict
city_dict=get_city_dict()
#打印所有的城市名：
#for city_name in city_dict.keys():
#    print (city_name)

#将城市对应的区域信息保存到字典中：
def get_district_dict(url):
    district_dict={}
    #获取html页面 
    html=urlopen(url).read()
    bsobj=BeautifulSoup(html,"html5lib")
    roles=bsobj.find("div",{"data-role":"ershoufang"}).findChildren("a")
    for role in roles:
        district_url=role.get("href")
        district_name=role.get_text()
        #存到字典中
        district_dict[district_name]=district_url
    return district_dict


'''
    <div data-role="ershoufang">
              <div>
                <a href="https://sh.lianjia.com/ershoufang/pudong/" title="上海浦东在售二手房 ">浦东</a>
                <a href="https://sh.lianjia.com/ershoufang/minhang/" title="上海闵行在售二手房 ">闵行</a>
                <a href="https://sh.lianjia.com/ershoufang/baoshan/" title="上海宝山在售二手房 ">宝山</a>
                <a href="https://sh.lianjia.com/ershoufang/xuhui/" title="上海徐汇在售二手房 ">徐汇</a>
                <a href="https://sh.lianjia.com/ershoufang/putuo/" title="上海普陀在售二手房 ">普陀</a>
'''
'''#设计与用户的交互：
input_city_name=input("请输入城市：")
city_url=city_dict.get(input_city_name)
if city_url:
    print (input_city_name,city_url)
else:
    print("输入错误")
    sys.exit()'''
# 与用户交互的设计的更新:
def run():
    city_dict=get_city_dict()
    #打印城市名
    for city in city_dict.keys():
        print(city,sep=' ')
    input_city_name=input("请输入城市：")
    city_url=city_dict.get(input_city_name)
    if not city_url:
        print("error input")
        sys.exit()
    ershoufang_city_url=city_url+"ershoufang"
    district_dict=get_district_dict(ershoufang_city_url)
    #打印区域名
    for district in district_dict.keys():
        print(district)
    
    input_district_name=input("请输入地区：")
    district_url=district_dict.get(input_district_name)
    if not district_url:
        print("error input")
        sys.exit()
    house_info_url=city_url+district_url[1:]
    print(house_info_url)
    house(house_info_url)

if __name__ =='__main__':
    run()