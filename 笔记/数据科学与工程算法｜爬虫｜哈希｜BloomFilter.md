# 数据科学与工程算法｜爬虫｜哈希｜BloomFilter

## 为什么要使用BloomFilter

判断我的小蜘蛛是不是一直在闭环上爬呀。

判断whether an element is in set or not.



## Hash

优点：HashMap有O(1)的检索效率～

缺点：存储容量占比高与哈希冲突

### HashAlgorithm

哈希算法是一个大杂烩，简单讲，哈希算法只需要把一个元素映射到另一个区间即可。

### 如何评价一个哈希算法的好坏？

评价一个哈希的好坏，通常会使用[SMHasher](https://github.com/aappleby/smhasher)

### Murmurhash

快速低碰撞的哈希算法，适用于一般的哈希检索操作。



## Bloom Filter 原理

一个超大的bit数组(m bit)和k个哈希函数

### 如何向过滤器中增加元素

1. 让该元素通过k个hashfunction
2. 得到位数组的k个位置
3. 将这k个位置都置为1.

### 查询

k位全是1才有可能存在(probalistic)的结果。

### 特点：

FalsePositive与(高召回)

我一定不会漏掉真的，但我可能把假的放进来。

### 如何确定m和k的大小?

即去寻找FalsePositiveRate与(m,k,n)的关系，这里n为元素的个数。

给定一个bit数组，一个元素经过k次hash都没有映射到该数组，即对于一个元素插入布隆的一次哈希映射，该数组被置为1的概率为$\frac{1}{m}$,没有被置为1的概率为$(1-\frac{1}{m})$,k次后，$(1-\frac{1}{m})^k$,插入n个元素后,该bit数组上该bit位上没有被置为1的概率为$(1-\frac{1}{m})^{nk}$，该bit数组上该bit位上被置为1的概率为$1-(1-\frac{1}{m})^{nk}$,而判断一个元素是否出现在bloom中需要k个bit位，所以$Pr(element \in Set(i.e._PFRate))=(1-(1-\frac{1}{m})^{nk})^k\approx(1-e^{-kn/m})^k$

> Question:为什么这个概率是PF_Rate？如何计算期望的PF_Rate?

### Python实现BloomFilter

详见bloomFilter.py

[参考代码](https://github.com/cpselvis/zhihu-crawler/blob/master/bloom_filter.py)





