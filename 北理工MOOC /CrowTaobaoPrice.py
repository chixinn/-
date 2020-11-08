#CrowTaobaoPrice.py
import requests
import re

def getHTMLText(url):
    try:
        header = {
            'authority': 's.taobao.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.61',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://www.taobao.com/',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cookie': 't=45617de446470fd44aee6d085f2d9e18; cna=SwSKFeQJLyYCATsqJmaw9KmK; miid=488275361906276349; tg=0; _m_h5_tk=7e994d481264fc9b7909a2fda08a7f77_1604587354537; _m_h5_tk_enc=dd8e40d0dd3512737c7a628d7ca28d87; v=0; _tb_token_=e3e5e7fbb0551; enc=d6kXYOkMlGO4Vpc3fpc0k15%2BptSme%2Fhs4qGftdmvi0gB595cZ8lCtM4ODRPLW8NsrIFzT1l8rh%2Fw974tqE3%2BKA%3D%3D; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; cookie2=14809c047547fa2b6897acb65a316e0f; hng=CN%7Czh-CN%7CCNY%7C156; xlly_s=1; thw=cn; _samesite_flag_=true; JSESSIONID=EA7B34945DCBBAC8990AED7A7D51BFFC; isg=BAsLXFa90HFmcQ6XrwKaebexmq_1oB8iJCKJQn0IP8oUnCn-BXX8cpZ9c5xy6Xca; l=eBj929xIqLsfyQIdBO5aourza77tzIRbzmFzaNbMiInca1uhtn6hnNQVmWH9SdtxgtCecetyM85CqdnprdadNxDDBexrCyCurxvO.; tfstk=cDaPBQx4raQrbrgCX4geVdyLTxiRaQ435ghKqkJ3LEs2KgqsQs4kpj4DB8eeH-nl.',
        }#由于淘宝网站的改进，现在要添加headers信息即可正确爬取
        r =requests.get(url,timeout = 30,headers=header)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""
def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price , title])
    except:
        print("")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))
        
def main():
    goods = '书包'
    depth = 3
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
    
main()
