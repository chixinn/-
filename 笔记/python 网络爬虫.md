

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

`<p class='title'>...</p>`属性域为了定义标签的特点。

`from bs4 import BeatifulSoup`

`import bs4`也可

> html Document//标签树//Beautiful Soup类是等价的

#### 解析器

`lxml/xml: pip install lxml`;`html5lib: pip install html5lib`

#### 基本元素

`tag.name/attrs/string`

```python
>>> tag.attrs
{'href': 'http://www.icourse163.org/course/BIT-268001', 'class': ['py1'], 'id': 'link1'}
```

`NavigableString`可以跨越多个标签层次。

#### 遍历功能（遍历的时候想象标签🌲）

`.contents||.children||.descendants||.parent`



### 如何让html文件更加“友好”

`print(soup.prettify())`

对标签的prettify`print(soup.a.prettify())`

bs4全部转换成了`utf-8`编码

### 标签树型结构：遍历的深入

![](https://tva1.sinaimg.cn/large/0081Kckwly1gkajn737xaj30x80g0h9l.jpg)

#### 下行遍历

- `.contents`儿子节点；返回列表
- `.children`
- `.descendants`

```python
>>> soup.body.contents
['\n', <p class="title"><b>The demo python introduces several python courses.</b></p>, '\n', <p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>, '\n']
>>> len(soup.body.contents)
5
```

遍历儿子节点与遍历子孙节点：

````python
for child in soup.body.children:
  print(child)  
````

#### 上行遍历

#### 平行遍历

必须发生在同一父节点下的各节点间。

平行遍历获得节点未必一定是标签类型(Navigable String)

#### soup变量中查找信息

`<>.find_all(name,attrs,recursive,string)`

查询多个标签`['a','b]`

####find_all 检索

![](https://tva1.sinaimg.cn/large/0081Kckwly1gkakgslbyaj30x80eqx33.jpg)

`soup.find_all(string='Basic Python')`要求我们进行精确的输入才可以检索。

> 使用正则表达式和find_all函数进行高效检索

`find_all`简写：

`<tag>(..)`等价于`<tag>.find_all(..)`;`<soup>(..)`等价于`<soup>.find_all(..)`;

##### 扩展方法：检索区域和返回个数不同

![](https://tva1.sinaimg.cn/large/0081Kckwly1gkakleia8xj30wi0fe15v.jpg)

### 三种信息标记形式(XML||JSON||YAML的比较

- XML:最早的信息标记语言，有强扩展性｜Internet上的信息交互与传递
- JSON:有类型的信息方式，比较适合**程序处理(js)**｜程序对接口处理的地方常用JSON，比较大的缺陷在于无注释，无法通过增加注释的信息
- YAML:各类系统的配置文件，文本信息比例最高，可读性好

###  信息提取的一般方法

#### 方法一:完整解析，再提取关键信息

如bs4标签树的遍历

#### 方法二：无视，然后直接采用搜索

直接应用信息的文本查找函数即可。

#### 即解析又搜索

![](https://tva1.sinaimg.cn/large/0081Kckwly1gkakzu5z3ej30ta0ack5a.jpg)

````python
soup.find_all(string='Basic Python')
['Basic Python']
>>> for link in soup.find_all('a'):
...     print(link.get('href'))
...
http://www.icourse163.org/course/BIT-268001
http://www.icourse163.org/course/BIT-1001870001
````

## 中国大学排名爬取

### 功能描述

Input: 大学排名URL链接

Output:排名信息的输出

技术路线：`requests-bs4`

爬虫类型：定向爬虫，即仅对输入URL进行爬取，而不进行拓展。

查看是否提供robots.txt

### 程序的结构设计

爬信息；找到合适的存放信息的数据结构

Python:二维列表。

### 定义函数

`def getHTMLText()`从网络上获取大学排名网页内容

`def fillUnivList()`提取网页内容中信息到合适的数据结构

`def printUnivList()`利用数据结构展示并输出结果

## 正则表达式Regular Expression//regex (RE)

> 简介表达一组本应该列出来的字符串

- 表达文本类型的特征(病毒、入侵)
- 同时查找或替换一组字符串
- 匹配字符串的全部或部分

> 主要是匹配

### 使用

编译：将符合正则表达式语法的字符串转换成正则表达式特征

### 语法

字符+操作符=正则表达式

- `.`：任何单个字符
- `[]`: 字符集，对**单个字符**给出取值范围
- `[^]`：对**单个字符**给出排除范围
- `*`: 0次到无限次扩展
- `+`：1次或无限次
- `?`：0次或1次
- `|`：左右表达式任意一个
- `{m}`:前一个m次
- `{m,n}`:前一个m至n次
- `^`:开头
- `$`:结尾m次
- `()`:分组标记
- `\d`:数字，等价于[0-9]
- `\w`：单词字符

### 实例

`^[A-Za-z]+$`：由26个字母组成的字符串

`^-?\d+$`:  整数形式的字符串

#### 匹配IP地址的正则表达式

0-99:`[1-9]?\d`;

![](https://tva1.sinaimg.cn/large/0081Kckwly1gkbudupclpj30ve0fsqgl.jpg)

### RE库的基本使用

`r'text'`

Raw string是指不包含转义符的字符串

> 当正则表达式包含转义符时，用raw string类型

`re.search()`;

![](https://tva1.sinaimg.cn/large/0081Kckwly1gkbuilgge6j30ve0e67g5.jpg)

### RE库的贪婪匹配与最小匹配

````python
>>> match =re.search(r'PY.*N','PYANBNCNDN')
>>> match.group(0)
````

> Re库默认采用贪婪匹配，即输出匹配最长的。

那么我们如何输出最短的？

```python
>>> match =re.search(r'PY.*?N','PYANBNCNDN')
>>> match.group(0)
```

![](https://tva1.sinaimg.cn/large/0081Kckwly1gkbvc267yxj30mq0ao7au.jpg)

![](https://tva1.sinaimg.cn/large/0081Kckwly1gkbvhgftkcj30mq0ao44z.jpg)

match对象只包含一次匹配的结果，如果想得到每一次，则需要finditer()函数。

![](https://tva1.sinaimg.cn/large/0081Kckwly1gkbvlxb981j30u00ao43r.jpg)