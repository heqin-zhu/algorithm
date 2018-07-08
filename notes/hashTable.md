---
title: 『数据结构』散列表
date: 2018-07-08  23:25
categories: 算法与数据结构
tags: [数据结构,散列表]
keywords:  
mathjax: true
description: 
---

哈希表 (hash table) , 可以实现 $O(1)$ 的 read, write, update
相对应 python 中的 dict, c语言中的 map

其实数组也能实现, 只是数组用来索引的关键字是下标, 是整数.
而哈希表就是将各种关键字映射到数组下标的一种"数组"

# 关键字
由于关键字是用来索引数据的, 所以要求它不能变动(如果变动,实际上就是一个新的关键字插入了), 在python 中表现为 imutable. 常为字符串.

# 映射
## 散列函数(hash)
将关键字 k 进行映射, 映射函数 $h$, 映射后的数组地址 $h(k)$.

### 简单一致散列

>* 简单一致假设:元素散列到每个链表的可能性是相同的, 且与其他已被散列的元素独立无关.
>* 简单一致散列(simple uniform hashing): 满足简单一致假设的散列

好的散列函数应 满足简单一致假设
例如
$$
\begin{aligned}
&(1)\quad h(k) = k \ mod\ m \\
&(2)\quad h(k) = \lfloor {m(kA \ mod\  1)\rfloor} = kA-\lfloor kA \rfloor \text{,\ x(0< A<  1)}\\
&\quad\text{任何 A 都使用,最佳的选择与散列的数据特征有关.}\\
&\quad\text{  Knuth 认为,最理想的是黄金分割数}\frac{\sqrt{5} -1}{2} \approx 0.618
\end{aligned}
$$

### 碰撞(collision)
 由于关键字值域大于映射后的地址值域, 所以可能出现两个关键字有相同的映射地址

### str2int 的方法
可以先用 ascii 值,然后
* 各位相加
* 两位叠加
* 循环移位
* ...


## 直接寻址法
将关键字直接对应到数组地址, 即 $h(k)=k$

缺点: 如果关键字值域范围大, 但是数量小, 就会浪费空间, 有可能还不能储存这么大的值域范围.



## 链接法
通过链接法来解决碰撞

![](https://upload-images.jianshu.io/upload_images/7130568-97d11b25923902c8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



记有 m 个链表, n 个元素 $\alpha = \frac{n}{m}$ 为每个链表的期望元素个数(长度)

则查找成功,或者不成功的时间复杂度为 $\Theta(1+\alpha)$
如果 $n=O(m), namely \quad \alpha=\frac{O(m)}{m}=O(1)$, 则上面的链接法满足 $O(1)$的速度



### 全域散列(universal hashing)
 随机地选择散列函数, 使之独立于要存储的关键字
#### 定义
设一组散列函数 $H=\{h_1,h_2,\ldots,h_i\}$, 将 关键字域 U 映射到 $\{0,1,\ldots,m-1\}$ , 全域的函数组, 满足
$$
for \ k \neq l \ \in U, h(k) = h(l), \text{这样的 h 的个数不超过}\frac{|H|}{m}
$$
即从 H 中任选一个散列函数, 当关键字不相等时, 发生碰撞的概率不超过 $\frac{1}{m}$

#### 性质
对于 m 个槽位的表, 只需 $\Theta(n)$的期望时间来处理 n 个元素的 insert, search, delete,其中  有$O(m)$个insert 操作
#### 实现
选择足够大的 prime p, 记$Z_p=\{0,1,\ldots,p-1\}, Z_p^*=\{1,\ldots,p-1\},$
令$h_{a,b}(k) = ((ak+b)mod\ p) mod\ m$
则 $H_{p,m}=\{h_{a,b}|a\in Z_p^*,b\in Z_p\}$
## 开放寻址法
所有表项都在散列表中, 没有链表.
且散列表装载因子$\alpha=\frac{n}{m}\leqslant1$
这里散列函数再接受一个参数, 作为探测序号
逐一试探 $h(k,0),h(k,1),\ldots,h(k,m-1)$,这要有满足的,就插入, 不再计算后面的 hash值

探测序列一般分有三种
* 线性$\ 0,1,\ldots,m-1$
存在一次聚集问题
* 二次$\ 0,1,\ldots,(m-1)^2$
存在二次聚集问题
* 双重探查
$h(k,i) = (h_1(k)+i*h_2(k))mod\ m$
为了能查找整个表, 即要为模 m 的完系, 则 h_2(k)要与 m 互质.
如可以取 $h_1(k) = k\ mod \ m,h_2(k) = 1+(k\ mod\ {m-1})$



注意删除时, 不能直接删除掉(如果有元素插入在其后插入时探测过此地址,删除后就不能访问到那个元素了), 应该 只是做个标记为删除

### 不成功查找的探查数的期望
对于开放寻址散列表,且 $\alpha<1$,在一次不成功的查找中,有 $E(\text{探查数})\leqslant \frac{1}{1-\alpha}$
不成功探查是这样的: 前面都是检查到槽被占用但是关键字不同, 最后一次应该是空槽.
![](https://upload-images.jianshu.io/upload_images/7130568-8d659aa8fe7de1a9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
#### 插入探查数的期望
所以, 插入一个关键字, 也最多需要 $\frac{1}{1-\alpha}$次, 因为插入过程就是前面都是被占用了的槽, 最后遇到一个空槽.与探查不成功是一样的过程
#### 成功查找的探查数的期望
成功查找的探查过程与插入是一样的. 所以查找关键字 k 相当于 插入它, 设为第 i+1 个插入的(前面插入了i个,装载因子$\alpha=\frac{i}{m}$. 那么期望探查数就是 
$$\frac{1}{1-\alpha}=\frac{1}{1-\frac{i}{m}}=\frac{m}{m-i}$$

则成功查找的期望探查数为
$$
\begin{aligned}
\frac{1}{n}\sum_{i=0}^{n-1}\frac{m}{m-i}=\frac{m}{n}\sum_{i=0}^{n-1}\frac{1}{m-i} &= \frac{m}{n}\sum_{i=m-n+1}^{m}\frac{1}{i}\\
&\leqslant  \frac{1}{\alpha} \int_{m-n}^m\frac{1}{x}dx\\
&=\frac{1}{\alpha}ln\frac{1}{1-\alpha}
\end{aligned}
$$
