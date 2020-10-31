

# python 网络爬虫

## Prerequsites

### HTTP协议与request库

#### HTTP协议

基于请求与相应模式的无状态的应用层协议.

Http协议使用**URL**对资源进行定位。

`http://www.bit.edu.cn`

#### URL

通过HTTP协议存取资源的Internet路径

`requests.request()//requests.get()//requests.head()//requests.patch//requests.post()`

### HTTP对资源的操作

![](https://tva1.sinaimg.cn/large/0081Kckwly1gk88bcqknfj30xi0jkqs6.jpg)

- GET/HEAD：获取URL位置的资源；一个是完整资源一个是头部资源(HEAD)
- PUT/POST/PATCH：POST(新增用户所提交的资源）PUT(将我们自己的资源提交上去)PATCH(URL位置的资源局部更新)上传资源；PATCH c.f.PUT 节省网络带宽
- POST:提交新增数据
- DELETE：删除

#### 理解r=requests.get(url)

![](https://tva1.sinaimg.cn/large/0081Kckwly1gk88oocxj4j30sk0bk18f.jpg)

#### request对象的属性

![](https://tva1.sinaimg.cn/large/0081Kckwly1gk89bwt0byj30sk0dmdox.jpg)

- r.status_code:只有200是对的
- r.text
- r.encoding
- r.apparent_encoding
- r.content

#### 基本流程

首先检查r.status_code:200

#### 理解两种编码(r.encoding与r.apparent_encoding)

![](https://tva1.sinaimg.cn/large/0081Kckwly1gk89f8pdijj30sk0baalu.jpg)

Apparent_encoding：实实在在的分析内容并找到其中可能的编码。

#### 爬取网页的通用代码框架

```python
try:
  r=requests.get(url,timeout=30)
  r.raise_for_status()#如果返回的对象返回code不是200，则产生异常
  r.encoding=r.apparent_encoding
  return r.text
except:
  return "产生异常"
```

​	网络链接有风险，异常处理很重要。

## 爬取网页的通用代码框架

### 网络链接有风险，异常处理很重要。

![](https://tva1.sinaimg.cn/large/0081Kckwly1gk89rrtivqj30sk0c6k0j.jpg)

对比ConnectTimeout与Timeout

response=r.raise_for_status()

## Robots协议

网站告知哪些可抓取，哪些不可抓取

形式：在网站根目录下的`robots.txt`

### Robots协议基本语法

````python

User-agent: *  ## '*'通配符代表所有
Disallow:/     ## '/'代表根目录
````

Robots协议一定放在网络的根目录下。

> 类人类行为可以不遵守robots协议

## Instance

### 爬反爬：为什么爬取亚马逊产品详情页是status_code:503?

`r.request.headers
{'User-Agent': 'python-requests/2.24.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}`

我们的爬虫忠实地告诉了Amazon被亚马逊的来源审查防掉了。

对于这种，可以通过更改headers信息模拟浏览器的访问请求。

`kv={'User-Agent':'Mozilla/5.0'}` Mozilla/5.0是**标准的浏览器身份**标示字段。

`r=requests.get("https://www.amazon.cn/b?_encoding=UTF8&node=2331388071&pf_rd_i=116169071&pf_rd_m=A1AJ19PSB66TGU&pf_rd_p=a01c2930-f21a-4158-8917-75a8d8a6c3cd&pf_rd_r=M67RCRQE6JD4DT3YGRKS&pf_rd_s=tcg-slide-1&pf_rd_t=101&ref_=ch_auto_pc_slides",headers=kv)`

`r.status_code:200`

` r.request.headers
{'User-Agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}`

### 百度/360搜索引擎的关键词提交

#### 搜索引擎关键词提交接口（post)

`http://www.baidu.com/s?wd=keyword`

对于参数额外使用

1. 首先构造参数：

   `kv={'wd':'Python'}`

2. `r=requests.get(url,params=kv)`

3. 此时我们使用`r.request.url`查看，发现自动帮我们补全成`http://www.baidu.com/s?wd=Python`

4. 那么我们如何解析r.text中返回的链接与内容呢？

   下回分解www

### 网络图片的爬取和存储

### 网络图片链接的格式

`http://www.example.com/picture.jpg`

获取之后再把图片写入到本地path即可。

```python
import requests
import os
url='demo_url'
root='path_root'
path=root+url.split('/')[-1]
try:
  if not os.path.exists(root):
    os.mkdir(root)
  if not os.path.exists(path):
    r=requests.get(url)
    with open(path,'wb') as f:
      f.write(r.content)#0101010100110010111
      f.close()
      print("File Saved Succeed!")
  else:
    print("File Exits!")
except:
  print("File Get error")

```

> 注意工程要求上的代码的可靠和稳定。

图片资源类比视频动画等，则即可获取网络很多资源。

## IP地址归属地的自动查询

[ip地址的查询网站](www.ip138.com)

### 解析接口：自动向网站提交时要挖掘网络后台的API

> 解析数据时最好要约束一下范围空间～
>
> 如r.text[-500]

## 如何解析HTML页面&信息标记与提取方法(BeautifulSoup)

`soup=BeautifulSoup(resoures_to_parse,'html.parser')`

### BeatifulSoup库的理解

