

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

