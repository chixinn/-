#通过获取的url获取该页面中该地区二手房的信息
# 注意爬虫要控制访问速度，不然会被网络管理员发现:D
import sys
import re
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

#成功打开页面时返回页面对象，否则打印错误信息
def get_bsobj(url):
    page=urllib.urlopen(url)
    #状态码为200时页面成功打开
    if page.getcode()==200:
        html=page.read()
        bsobj=BeautifulSoup(html,"html5lib")
        return bsobj
    else:
        print("Error")
        sys.exit()

#将页面中每一条房屋信息保存为一个字典
def get_house_info_list(url):
    house_info_list=[]
    bsobj=get_bsobj(url)
    if not bsobj:
        return None
    house_list=bsobj.find_all("div",{"class":"item"})#?

    for house in house_list:
        title=house.find("div",{"class":"title"}).get_text()
        #获取信息数据
        info =house.find("div",{"class":"info"}).get_text().split("/")#or <span>/</span>?
        '''
        <div class="info">曹杨<span>/</span>
        2室1厅<span>/</span>69.34平米<span>/</span>
        南<span>/</span>精装</div>

        '''
        block=info[0].strip()
        house_type=info[1].strip()
        size_info=info[2].strip()
        size=re.findall(r"\d+",size_info)[0]
        price_info=house.find("div", {"class":"price"}).span.get_text()
        price=re.findall(r"\d+",price_info)[0]
        #添加到列表中
        house_info_list.append({
            "title":title,
            "price":int(price)
            "size":int(size)
            "block":block,
            "house_type":house_type
        })
        return house_info_list
def house(url):
    house_info_list=[]
    for i in range(3):
        new_url=url+'pg'+str(i+1)
        house_info_list.extend(get_house_info_list(new_url))
    if house_info_list:
        with open("./house.csv","wb+") as f:
            writer =csv.writer(f,delimiter='|')
            for house_info in house_info_list:
                title=house_info.get("title")
                price=house_info.get("price")
                size=house_info.get("size")
                block=house_info.get("block")
                house_type=house_info.get("house_type")
                writer.writerow([title,int(price),int(size),block,house_type])
                print(block,price,size)
