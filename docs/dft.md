---
title: 傅里叶变换
date: 2019-06-10  23:46
categories: 数学
tags: [数学, 图像处理]
keywords: FFT, 傅里叶变换, 图像处理 
mathjax: true
description: 
    图像处理中, 为了方便处理，便于抽取特征，数据压缩等目的，常常要将图形进行变换,这篇文章介绍一下傅里叶变换
---
<!-- TOC -->

- [定义](#定义)
    - [连续](#连续)
    - [离散](#离散)
- [性质](#性质)
    - [分离性](#分离性)
    - [位移定理](#位移定理)
    - [周期性](#周期性)
    - [共轭对称性](#共轭对称性)
    - [旋转性](#旋转性)
    - [加法定理](#加法定理)
    - [平均值](#平均值)
    - [相似性定理](#相似性定理)
    - [卷积定理](#卷积定理)
    - [相关定理](#相关定理)
    - [Rayleigh 定理](#rayleigh-定理)
- [快速傅里叶变换](#快速傅里叶变换)
    - [复数中的单位根](#复数中的单位根)
    - [快速傅里叶变换的计算](#快速傅里叶变换的计算)
- [代码](#代码)
- [参考](#参考)

<!-- /TOC -->


图像处理中, 为了方便处理，便于抽取特征，数据压缩等目的，常常要将图像进行变换。
一般有如下变换方法
1. 傅立叶变换Fourier Transform 
2. 离散余弦变换Discrete Cosine Transform 
3. 沃尔希-哈德玛变换Walsh-Hadamard Transform 
4. 斜变换Slant Transform 
5. 哈尔变换Haar Transform 
6. 离散K-L变换Discrete Karhunen-Leave Transform 
7. 奇异值分解SVD变换Singular-Value Decomposition 
8. 离散小波变换Discrete Wavelet Transform 

这篇文章介绍一下傅里叶变换



## 定义
### 连续
积分形式
如果一个函数的绝对值的积分存在，即
![](https://latex.codecogs.com/gif.latex?&space;\int_{-\infty}&space;^\infty&space;|h(t)|dt<\infty&space;)
并且函数是连续的或者只有有限个不连续点，则对于 x 的任何值， 函数的傅里叶变换存在
- 一维傅里叶变换
![](https://latex.codecogs.com/gif.latex?&space;H(f)=\int_{-\infty}&space;^\infty&space;h(t)e^{-j2\pi&space;ft}dt&space;)
- 一维傅里叶逆变换
![](https://latex.codecogs.com/gif.latex?&space;H(f)=\int_{-\infty}&space;^\infty&space;h(t)e^{j2\pi&space;ft}dt&space;)
同理多重积分
### 离散
实际应用中，多用离散傅里叶变换 DFT.
- 一维傅里叶变换
![](https://latex.codecogs.com/gif.latex?&space;F(u)=\sum_{x=0}&space;^{N-1}&space;f(x)e^{\frac{-2\pi&space;j}{N}&space;ux}&space;)
- 一维傅里叶逆变换
![](https://latex.codecogs.com/gif.latex?&space;f(x)=\frac{1}{N}\sum_{u=0}&space;^{N-1}&space;F(u)e^{\frac{2\pi&space;j}{N}&space;ux}&space;)
需要注意的是， 逆变换乘以 ![](https://latex.codecogs.com/gif.latex?\frac{1}{N}) 是为了**归一化**，这个系数可以随意改变， 即可以正变换乘以 ![](https://latex.codecogs.com/gif.latex?\frac{1}{N}), 逆变换就不乘，或者两者都乘以![](https://latex.codecogs.com/gif.latex?\frac{1}{\sqrt{N}})等系数。
- 二维傅里叶变换
![](https://latex.codecogs.com/gif.latex?&space;F(u,v)=\frac{1}{N}\sum_{x=0}^{N-1}\sum_{y=0}&space;^{N-1}&space;f(x,y)e^{\frac{-2\pi&space;j}{N}&space;(ux+vy)}&space;)
- 二维傅里叶逆变换

![](https://latex.codecogs.com/gif.latex?&space;f(x,y)=\frac{1}{N}\sum_{u=0}^{N-1}\sum_{v=0}&space;^{N-1}&space;F(u,v)e^{\frac{2\pi&space;j}{N}&space;(ux+vy)}&space;)

幅度
![](https://latex.codecogs.com/gif.latex?&space;|F(u,v)|&space;=&space;\sqrt{real(F)^2+imag(F)^2}&space;)
相位
![](https://latex.codecogs.com/gif.latex?&space;arctan{\frac{imag(F)}{real(F)}}&space;)
对于图像的幅度谱显示，由于 |F(u,v)| 变换范围太大，一般显示 ![](https://latex.codecogs.com/gif.latex?D=&space;log(|F(u,v)+1))

用 `<=>` 表示傅里叶变换对
![](https://latex.codecogs.com/gif.latex?&space;f(x)<=>F(u)\\&space;f(x,y)<=>F(u,v)&space;)

f,g,h 对应的傅里叶变换 F,G,H

![](https://latex.codecogs.com/gif.latex?F^*) 表示 ![](https://latex.codecogs.com/gif.latex?F) 的共轭
## 性质
### 分离性
![](https://latex.codecogs.com/gif.latex?&space;\begin{aligned}&space;&F(x,v)=\sum_{y=0}&space;^{N-1}&space;f(x,y)e^{\frac{-2\pi&space;j}{N}&space;vy}\\&space;&F(u,v)=\frac{1}{N}\sum_{x=0}^{N-1}F(x,v)e^{\frac{-2\pi&space;j}{N}ux}&space;\end{aligned}&space;)
进行多维变换时，可以依次对每一维进行变换。 下面在代码中就是这样实现的。
### 位移定理
![](https://latex.codecogs.com/gif.latex?&space;f(x,y)e^{\frac{2\pi&space;j}{N}(u_0x+v_0y)}&space;<=>F(u-u_0,v-v_0)&space;)
![](https://latex.codecogs.com/gif.latex?&space;f(x-x_0,y-y_0)<=>F(u,v)e^{\frac{-2\pi&space;j}{N}(ux_0+vy_0)}&space;)

### 周期性
![](https://latex.codecogs.com/gif.latex?&space;F(u,v)&space;=&space;F(u+N,v+N)&space;)
### 共轭对称性
![](https://latex.codecogs.com/gif.latex?F(u,v)&space;=&space;F^*(-u,-v))
a)偶分量函数在变换中产生偶分量函数; 
b)奇分量函数在变换中产生奇分量函数; 
c)奇分量函数在变换中引入系数-j; 
d)偶分量函数在变换中不引入系数. 

### 旋转性
if ![](https://latex.codecogs.com/gif.latex?&space;f(r,\theta)<=>F(\omega,\phi)&space;)
then ![](https://latex.codecogs.com/gif.latex?f(r,\theta+t)<=>F(\omega,\phi+t)&space;)
### 加法定理
1.
![](https://latex.codecogs.com/gif.latex?&space;Fourier[f+g]=Fourier[f]+Fourier[g]&space;)
2.
![](https://latex.codecogs.com/gif.latex?&space;af(x,y)<=>aF[u,v]&space;)

### 平均值
![](https://latex.codecogs.com/gif.latex?&space;\frac{1}{N^2}\sum_{x=0}^{N-1}\sum_{y=0}&space;^{N-1}&space;f(x,y)&space;=&space;\frac{1}{N}F(0,0)&space;)
### 相似性定理
尺度变换
![](https://latex.codecogs.com/gif.latex?&space;f(ax,by)<=>\frac{F(\frac{u}{a},\frac{v}{b})}{ab}&space;)

### 卷积定理
卷积定义
1d
![](https://latex.codecogs.com/gif.latex?&space;f*g&space;=&space;\frac{1}{M}\sum_{m=0}^{M-1}f(m)g(x-m)&space;)
2d
![](https://latex.codecogs.com/gif.latex?&space;f(x,y)*g(x,y)&space;=&space;\frac{1}{MN}\sum_{m=0}^{M-1}\sum_{n=0}^{N-1}f(m,n)g(x-m,y-n)&space;)

卷积定理
![](https://latex.codecogs.com/gif.latex?&space;f(x,y)*g(x,y)&space;<=>&space;F(u,v)G(u,v)&space;)
![](https://latex.codecogs.com/gif.latex?&space;f(x,y)g(x,y)<=>F(u,v)*G(u,v)&space;)

离散卷积
用
![](https://latex.codecogs.com/gif.latex?&space;\sum_{i=0}^{N-1}x(iT)h[(k-i)T]&space;<=>&space;X(\frac{n}{NT})H(\frac{n}{NT})&space;)
即两个周期为 N 的抽样函数， 他们的卷积的离散傅里叶变换等于他们的离散傅里叶变换的卷积

卷积的应用：
去除噪声， 特征增强
两个不同周期的信号卷积需要周期扩展的原因：如果直接进行傅里叶变换和乘积，会产生折叠误差(卷绕)。

### 相关定理
下面用![](https://latex.codecogs.com/gif.latex?\infty) 表示相关。
相关函数描述了两个信号之间的相似性，其相关性大小有相关系数衡量

- 相关函数的定义
离散
![](https://latex.codecogs.com/gif.latex?f(x,y)\quad&space;\infty&space;\quad&space;g(x,y)&space;=&space;\frac{1}{MN}\sum_{m=0}^{M-1}\sum_{n=0}^{N-1}f^*(m,n)g(x+m,y+n)&space;)
连续
![](https://latex.codecogs.com/gif.latex?z(t)&space;=&space;\int_{-\infty}^{\infty}x^*(\tau)&space;h(t+\tau)d\tau)
- 定理
![](https://latex.codecogs.com/gif.latex?&space;f(x,y)\quad&space;\infty&space;\quad&space;g(x,y)<=>F^*(u,v)G(u,v)&space;)
### Rayleigh 定理
能量变换
对于有限区间非零函数 f(t), 其能量为
![](https://latex.codecogs.com/gif.latex?&space;E&space;=&space;\int_{-\infty}^{\infty}|f(t)|^2dt&space;)

其变换函数与原函数有相同的能量
![](https://latex.codecogs.com/gif.latex?&space;\int_{-\infty}^{\infty}|f(t)|^2dt&space;=&space;\int_{-\infty}^{\infty}|F(u)|^2dt&space;)
## 快速傅里叶变换
由上面离散傅里叶变换的性质易知，直接计算 1维 dft 的时间复杂度维 ![](https://latex.codecogs.com/gif.latex?O(N^2))。

利用到单位根的对称性，快速傅里叶变换可以达到 ![](https://latex.codecogs.com/gif.latex?O(nlogn))的时间复杂度。


### 复数中的单位根
我们知道， 在复平面，复数 ![](https://latex.codecogs.com/gif.latex?cos\theta&space;+i\&space;sin\theta)k可以表示成 ![](https://latex.codecogs.com/gif.latex?e^{i\theta})， 可以对应一个向量。![](https://latex.codecogs.com/gif.latex?\theta)即为幅角。
 在**单位圆**中 ，单位圆被分成 ![](https://latex.codecogs.com/gif.latex?\frac{2\pi}{\theta}) 份， 由单位圆的对称性 
![](https://latex.codecogs.com/gif.latex?&space;e^{i\theta}&space;=&space;e^{i(\theta+2\pi)}&space;)
现在记 ![](https://latex.codecogs.com/gif.latex?n&space;=\frac{&space;2\pi&space;}{\theta}) ， 即被分成 n 份，幅度角为正且最小的向量称为 n 次单位向量， 记为![](https://latex.codecogs.com/gif.latex?\omega&space;_n)，
其余的 n-1 个向量分别为 ![](https://latex.codecogs.com/gif.latex?\omega_{n}^{2},\omega_{n}^{3},\ldots,\omega_{n}^{n}) ，它们可以由复数之间的乘法得来 ![](https://latex.codecogs.com/gif.latex?w_{n}^{k}=w_{n}^{k-1}\cdot&space;w_{n}^{1}\&space;(2&space;\leq&space;k&space;\leq&space;n))。
单位根的性质
1. 这个可以用 e 表示出来证明
![](https://latex.codecogs.com/gif.latex?&space;\omega_{2n}^{2k}=\omega_{n}^{k}&space;)
2. 可以写成三角函数证明
![](https://latex.codecogs.com/gif.latex?&space;\omega_{n}^{k+\frac{n}{2}}=-\omega_{n}^{k}&space;)

容易看出 ![](https://latex.codecogs.com/gif.latex?w_{n}^{n}=w_{n}^{0}=1)。

对于![](https://latex.codecogs.com/gif.latex?w_{n}^{k}) , 它事实上就是 ![](https://latex.codecogs.com/gif.latex?e^{\frac{2\pi&space;i}{n}k}) 。
### 快速傅里叶变换的计算
下面的推导假设 ![](https://latex.codecogs.com/gif.latex?n=2^k)，以及代码实现 FFT 部分也是 如此。

利用上面的对称性，
将傅里叶计算进行奇偶分组
![](https://latex.codecogs.com/gif.latex?&space;\begin{aligned}&space;F(u)&=\sum_{i=0}^{n-1}\omega_n&space;^{iu}&space;a^i\\&space;&=&space;\sum_{i=0}^{\frac{n}{2}-1}\omega_n&space;^{2iu}&space;a^{2i}+\sum_{i=0}^{\frac{n}{2}-1}\omega_n&space;^{(2i+1)u}&space;a^{2i+1}\\&space;&=\sum_{i=0}^{\frac{n}{2}-1}\omega_{\frac{n}{2}}&space;^{iu}&space;a^{2i}+\omega_n^u\sum_{i=0}^{\frac{n}{2}-1}\omega_{\frac{n}{2}}&space;^{iu}&space;a^{2i+1}\\&space;&&space;=&space;F_{even}(u)+\omega_n^u&space;F_{odd}(u)&space;\end{aligned}&space;)
![](https://latex.codecogs.com/gif.latex?F_{even})表示将 输入的次序中偶数点进行 Fourier 变换， ![](https://latex.codecogs.com/gif.latex?F_{odd}) 同理，这样就形成递推公式。
现在还没有减少计算量，下面通过将分别计算的 奇项，偶项利用起来，只计算 前 ![](https://latex.codecogs.com/gif.latex?\frac{n}{2}-1)项，后面的一半可以利用此结果马上算出来。每一次可以减少一半的计算量。

对于 ![](https://latex.codecogs.com/gif.latex?\frac{n}{2}\leq&space;i+\frac{n}{2}\leq&space;n-1)
![](https://latex.codecogs.com/gif.latex?&space;\begin{aligned}&space;F(\omega_{n}^{i+\frac{n}{2}})&=F_{even}(\omega_{n}^{2i+n})+\omega_{n}^{i+\frac{n}{2}}\cdot&space;F_{odd}(\omega_{n}^{2i+n})\\&space;&=F_{even}(\omega_{\frac{n}{2}}^{i+\frac{n}{2}})+\omega_{\frac{n}{2}}^{i+\frac{n}{2}}\cdot&space;F_{odd}(\omega_{\frac{n}{2}}^{i+\frac{n}{2}})\\&space;&&space;=F_{even}(\omega_{\frac{n}{2}}^{i})-\omega_{\frac{n}{2}}^{i}\cdot&space;F_{odd}(\omega_{\frac{n}{2}}^{i})&space;\end{aligned}&space;)
现在很清楚了，在每次计算 a[0..n-1] 的傅里叶变换F[0..n-1]，分别计算出奇 odd[0..n/2-1]，偶even[0..n/2-1]（可以递归地进行），
那么傅里叶变换为：
![](https://latex.codecogs.com/gif.latex?&space;F[i]&space;=&space;\begin{cases}&space;even[i]+&space;\omega^i&space;\cdot&space;odd[i],&space;\quad&space;i<\frac{n}{2}\\&space;even[i]-&space;\omega^i&space;\cdot&space;odd[i],&space;\quad&space;else&space;\end{cases}&space;)

## 代码
下面是 python 实现
一维用 FFT 实现， 不过 只实现了 2 的幂。/ 对于非 2 的幂，用 FFT 实现有点困难，还需要插值，所以我 用![](https://latex.codecogs.com/gif.latex?O(n^2)) 直接实现。

二维的 DFT利用 分离性，直接调用 一维 FFT。
[GitHub](https://github.com/mbinary/algorithm)

```python
import numpy as np


def _fft(a, invert=False):
    N = len(a)
    if N == 1:
        return [a[0]]
    elif N & (N - 1) == 0:  # O(nlogn),  2^k
        even = _fft(a[::2], invert)
        odd = _fft(a[1::2], invert)
        i = 2j if invert else -2j
        factor = np.exp(i * np.pi * np.arange(N // 2) / N)
        prod = factor * odd
        return np.concatenate([even + prod, even - prod])
    else:  # O(n^2)
        w = np.arange(N)
        i = 2j if invert else -2j
        m = w.reshape((N, 1)) * w
        W = np.exp(m * i * np.pi / N)
        return np.concatenate(np.dot(W, a.reshape(
            (N, 1))))  # important, cannot use *


def fft(a):
    '''fourier[a]'''
    n = len(a)
    if n == 0:
        raise Exception("[Error]: Invalid length: 0")
    return _fft(a)


def ifft(a):
    '''invert fourier[a]'''
    n = len(a)
    if n == 0:
        raise Exception("[Error]: Invalid length: 0")
    return _fft(a, True) / n


def fft2(arr):
    return np.apply_along_axis(fft, 0,
                               np.apply_along_axis(fft, 1, np.asarray(arr)))


def ifft2(arr):
    return np.apply_along_axis(ifft, 0,
                               np.apply_along_axis(ifft, 1, np.asarray(arr)))


def test(n=128):
    print('\nsequence length:', n)
    print('fft')
    li = np.random.random(n)
    print(np.allclose(fft(li), np.fft.fft(li)))

    print('ifft')
    li = np.random.random(n)
    print(np.allclose(ifft(li), np.fft.ifft(li)))

    print('fft2')
    li = np.random.random(n * n).reshape((n, n))
    print(np.allclose(fft2(li), np.fft.fft2(li)))

    print('ifft2')
    li = np.random.random(n * n).reshape((n, n))
    print(np.allclose(ifft2(li), np.fft.ifft2(li)))


if __name__ == '__main__':
    for i in range(1, 3):
        test(i * 16)
```

## 参考
- [万寿红老师课件]()
- [一小时学会快速傅里叶变换 Fast Fourier Transform](https://zhuanlan.zhihu.com/p/31584464)
- [快速傅里叶变换（FFT）算法【详解】](https://www.cnblogs.com/ECJTUACM-873284962/p/6919424.html)


