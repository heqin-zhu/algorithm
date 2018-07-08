---
title: 『算法』general
date: 2018-07-04
categories: 算法与数据结构
tags: [算法]
keywords: 
mathjax: true
top:  
---
<!-- TOC -->

- [1. 算法](#1-算法)
- [2. 可以解决哪些类型的问题](#2-可以解决哪些类型的问题)
- [3. 算法分析](#3-算法分析)
- [4. 算法设计](#4-算法设计)
    - [4.1. 分治(divide and conquer)](#41-分治divide-and-conquer)
- [5. 递归式](#5-递归式)
    - [5.1. 代换法](#51-代换法)
        - [5.1.1. 步骤](#511-步骤)
        - [5.1.2. 例子](#512-例子)
        - [5.1.3. 放缩](#513-放缩)
        - [5.1.4. 改变变量](#514-改变变量)
    - [5.2. 递归树](#52-递归树)
    - [5.3. 主方法(master method)](#53-主方法master-method)
        - [5.3.1. 记忆](#531-记忆)
        - [5.3.2. 证明](#532-证明)
            - [5.3.2.1. 证明当 n 为 b 的正合幂时成立](#5321-证明当-n-为-b-的正合幂时成立)
            - [5.3.2.2. 分析扩展至所有正整数 n 都成立](#5322-分析扩展至所有正整数-n-都成立)
- [6. 随机算法](#6-随机算法)
    - [6.1. 随机排列数组(shuffle)](#61-随机排列数组shuffle)
        - [6.1.1. PERMUTE-BY-SORTING](#611-permute-by-sorting)
        - [6.1.2. RANDOMIZE-IN-PLACE](#612-randomize-in-place)
- [7. 组合方程的近似算法](#7-组合方程的近似算法)
- [8. 概率分析与指示器变量例子](#8-概率分析与指示器变量例子)
    - [8.1. 球与盒子](#81-球与盒子)
    - [8.2. 序列](#82-序列)

<!-- /TOC -->

<a id="markdown-1-算法" name="1-算法"></a>
# 1. 算法
定义良好的计算过程,取输入,并产生输出. 即算法是一系列的计算步骤,将输入数据转化为输出结果

<a id="markdown-2-可以解决哪些类型的问题" name="2-可以解决哪些类型的问题"></a>
# 2. 可以解决哪些类型的问题
* 大数据的存储,以及开发出进行这方面数据分析的工具
* 网络数据的传输,寻路, 搜索
* 电子商务密码, (数值算法,数论)
* 资源分配,最大效益
* ...

<a id="markdown-3-算法分析" name="3-算法分析"></a>
# 3. 算法分析
衡量算法的优劣
![](https://upload-images.jianshu.io/upload_images/7130568-d452e7efb6fb3433.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


* $\omicron,O,\Omega,\Theta$
* 最坏情况, 平均情况
* 增长的量级$ O(1),O(logn), O(n), O(n^k), O(a^n) $


<a id="markdown-4-算法设计" name="4-算法设计"></a>
# 4. 算法设计
<a id="markdown-41-分治divide-and-conquer" name="41-分治divide-and-conquer"></a>
## 4.1. 分治(divide and conquer)
结构上是递归的,
步骤: 分解,解决, 合并
eg 快排,归并排序

<a id="markdown-5-递归式" name="5-递归式"></a>
# 5. 递归式
 $T(n) = aT(\frac{n} {b})+f(n)$

<a id="markdown-51-代换法" name="51-代换法"></a>
## 5.1. 代换法
<a id="markdown-511-步骤" name="511-步骤"></a>
### 5.1.1. 步骤
* 猜测解的形式
* 用数学归纳法找出常数
<a id="markdown-512-例子" name="512-例子"></a>
### 5.1.2. 例子
$T(n) = 2T(\frac{n} {2})+n$
猜测$T(n) = O(nlogn)$
证明 $ T(n)\leqslant cnlogn$
归纳奠基 n=2,3
归纳假设 $T(\frac{n} {2}) \leqslant \frac{cn}{2}$
递归   
$
\begin{aligned}
T(n) &\leqslant  2c\frac{n}{2}log(\frac{n}{2}) + n \leqslant cnlog(\frac{n}{2})  \\
\end{aligned}
$
<a id="markdown-513-放缩" name="513-放缩"></a>
### 5.1.3. 放缩
对于 $T(n) = 2T(\frac{cn}{2}) + 1$
如果 直接猜测 $T(n) =  O (n)$ 不能证明, 
而且不要猜测更高的界 $O (n^2)$
可以放缩为 n-b
<a id="markdown-514-改变变量" name="514-改变变量"></a>
### 5.1.4. 改变变量
对于 $ T(n) = 2T(\sqrt{n})+logn $
可以 令 `m = logn`, 得到
$T(2^m) = 2T(m^{\frac{m}{2}}) + m $
令 $S(m) = T(2^m)$
得到 $ S(m) = 2S(\frac{m}{2}) + m $

<a id="markdown-52-递归树" name="52-递归树"></a>
## 5.2. 递归树
例如 $T(n) = 3T(\frac{n}{4}) + c n^2$
不妨假设 n 为4的幂, 则有如下递归树
![recursive-tree.jpg](https://upload-images.jianshu.io/upload_images/7130568-4a1b9b6ee852b725.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



每个结点是代价, 将每层加起来即可

<a id="markdown-53-主方法master-method" name="53-主方法master-method"></a>
## 5.3. 主方法(master method)
对于 $T(n) = aT(\frac{n} {b})+f(n)$
$$
\begin{aligned}
T(n)=\begin{cases}
\Theta(n^{log_b a}),\quad f(n)=O(n^{ {log_b a}-\epsilon})   \\
\Theta(n^{log_b a}logn),\quad  f(n)=\Theta(n^{log_b a})   \\
\Theta(f(n)),\quad f(n)=\Omega(n^{ {log_b a}+ \epsilon}),af(\frac{n}{b})\leqslant cf(n)  \\
\qquad \qquad \quad  \text{其中常数c<1,变量n任意大}    \\
unknown, \quad others
\end{cases}
\end{aligned}
$$
<a id="markdown-531-记忆" name="531-记忆"></a>
### 5.3.1. 记忆
直观上, 比较 $n^{log_b a}$ 和 $f(n)$, 谁大就是谁, 
这里的大是多项式上的比较, 即比较次数, 而不是渐近上的
比如 $n$ 与 $nlogn$ 渐近上后者大, 但多项式上是不能比较的

<a id="markdown-532-证明" name="532-证明"></a>
### 5.3.2. 证明
<a id="markdown-5321-证明当-n-为-b-的正合幂时成立" name="5321-证明当-n-为-b-的正合幂时成立"></a>
#### 5.3.2.1. 证明当 n 为 b 的正合幂时成立
* 用递归树可以得到 总代价为 $\sum_{j=0}^{log_b n-1} a^j f(\frac{n}{b^j})$
* 决定上式的渐近界
* 结合前两点

<a id="markdown-5322-分析扩展至所有正整数-n-都成立" name="5322-分析扩展至所有正整数-n-都成立"></a>
#### 5.3.2.2. 分析扩展至所有正整数 n 都成立
主要是应用数学技巧来解决 floor, ceiling 函数的处理问题

<a id="markdown-6-随机算法" name="6-随机算法"></a>
# 6. 随机算法
<a id="markdown-61-随机排列数组shuffle" name="61-随机排列数组shuffle"></a>
## 6.1. 随机排列数组(shuffle)
<a id="markdown-611-permute-by-sorting" name="611-permute-by-sorting"></a>
### 6.1.1. PERMUTE-BY-SORTING
给出初始数组, eg A={1,2,3}, 选择随机的优先级 P={16,4,10}
则得出 B={2,3,1},因为第二个(2)优先级最小, 为4, 接着第三个,最后第1个.
优先级数组的产生, 一般在 RANDOM(1,n^3), 这样优先级各不相同的概率至少为 1-1/n

由于要排序优先级数组, 所以时间复杂度 $O(nlogn)$

如果优先级唯一,  则此算法可以 shuffle 数组
应证明 同样排列的概率是 $\frac{1}{n!}$

<a id="markdown-612-randomize-in-place" name="612-randomize-in-place"></a>
### 6.1.2. RANDOMIZE-IN-PLACE
```python
# arr: array to be shuffled
n = len(arr)
for i in range(n):
    swap(arr[i],arr[random(i,n-1)])
```
时间复杂度 $O(n)$
证明
定义循环不变式: 对每个可能的 $A_n^{i-1}$ 排列, 其在 arr[1..i-1] 中的概率为 $\frac{1}{A_n^{i-1}}$
初始化: i=1 成立
保持 : 假设 在第 i-1 次迭代之前,成立, 证明在第 i 次迭代之后, 仍然成立,
终止: 在 结束后, i=n+1, 得到 概率为 $\frac{1}{n!}$
<a id="markdown-7-组合方程的近似算法" name="7-组合方程的近似算法"></a>
# 7. 组合方程的近似算法
* Stiring 's approximation: $ n! \approx \sqrt{2\pi n}\left(\frac{n}{e}\right)^n$
* 对于 $C_n^x=a$, 有 $x=\frac{ln^2 a}{n}$
* 对于 $C_x^n=a$, 有 $x=(a*n!)^{\frac{1}{n}}+\frac{n}{2}$

<a id="markdown-8-概率分析与指示器变量例子" name="8-概率分析与指示器变量例子"></a>
# 8. 概率分析与指示器变量例子
<a id="markdown-81-球与盒子" name="81-球与盒子"></a>
## 8.1. 球与盒子
把相同的秋随机投到 b 个盒子里,问在每个盒子里至少有一个球之前,平均至少要投多少个球?
称投入一个空盒为击中, 即求取得 b 次击中的概率
设投 n 次, 称第 i 个阶段包括第 i-1 次击中到 第 i 次击中的球, 则 $p_i=\frac{b-i+1}{b}$
用 $n_i$表示第 i 阶段的投球数,则 $n=\sum_{i=1}^b n_i$
且 $n_i$服从几何分布, $E(n_i)=\frac{b}{b-i+1}$,
则由期望的线性性, 
$$
E(n)=E(\sum_{i=1}^b n_i)=\sum_{i=1}^b E(n_i)=\sum_{i=1}^b \frac{b}{b-i+1}=b\sum_{i=1}^b \frac{1}{i}=b(lnb+O(1))
$$
这个问题又被称为 赠券收集者问题(coupon collector's problem),即集齐 b 种不同的赠券,在随机情况下平均需要买 blnb 张
<a id="markdown-82-序列" name="82-序列"></a>
## 8.2. 序列
抛 n 次硬币, 期望看到的连续正面的次数
答案是 $\Theta(logn)$
记 长度至少为 k 的正面序列开始与第 i 次抛, 由于独立, 所有 k 次抛掷都是正面的 概率为 
$P(A_{ik})=\frac{1}{2^k}$,对于 $k=2\lceil lgn\rceil$
![coin1.jpg](https://upload-images.jianshu.io/upload_images/7130568-780b9795b6d9a2bd.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![coin2.jpg](https://upload-images.jianshu.io/upload_images/7130568-7d112b304e2d78b6.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![coin3.jpg](https://upload-images.jianshu.io/upload_images/7130568-f104d530f2a57c99.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![coin4.jpg](https://upload-images.jianshu.io/upload_images/7130568-be0fd1b57a5ff305.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

