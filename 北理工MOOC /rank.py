#2020中国大学排名实例
from bs4 import BeautifulSoup
import bs4
import requests
import re
import pandas as pd

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''

def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag): #过滤非标签
            tds=tr.find_all('td')
            #学校省市在tds[1]下面的<a>
            #tds[0],tds[2]等需去除空格  
            ulist.append([tds[0].string.strip(),tds[1].find('a').string,tds[2].string.strip(),tds[3].string.strip(),tds[4].string.strip(),tds[5].string.strip()])

def list2DataFrame(list):
    print(pd.DataFrame(list,columns=('学校排名','学校名称','省市','类型','总分','办学层次')))

    
def main():
    uinfo=[]
    url='https://www.shanghairanking.cn/rankings/bcur/2020'
    html=getHTMLText(url)
    fillUnivList(uinfo,html)
    list2DataFrame(uinfo)

main()