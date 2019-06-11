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
$$
\int_{-\infty} ^\infty |h(t)|dt<\infty
$$
并且函数是连续的或者只有有限个不连续点，则对于 x 的任何值， 函数的傅里叶变换存在
- 一维傅里叶变换
$$
H(f)=\int_{-\infty} ^\infty h(t)e^{-j2\pi ft}dt
$$
- 一维傅里叶逆变换
$$
H(f)=\int_{-\infty} ^\infty h(t)e^{j2\pi ft}dt
$$
同理多重积分
### 离散
实际应用中，多用离散傅里叶变换 DFT.
- 一维傅里叶变换
$$
F(u)=\sum_{x=0} ^{N-1} f(x)e^{\frac{-2\pi j}{N} ux}
$$
- 一维傅里叶逆变换
$$
f(x)=\frac{1}{N}\sum_{u=0} ^{N-1} F(u)e^{\frac{2\pi j}{N} ux}
$$
需要注意的是， 逆变换乘以 $\frac{1}{N}$ 是为了**归一化**，这个系数可以随意改变， 即可以正变换乘以 $\frac{1}{N}$, 逆变换就不乘，或者两者都乘以$\frac{1}{\sqrt{N}}$等系数。
- 二维傅里叶变换
$$
F(u,v)=\frac{1}{N}\sum_{x=0}^{N-1}\sum_{y=0} ^{N-1} f(x,y)e^{\frac{-2\pi j}{N} (ux+vy)}
$$
- 二维傅里叶逆变换

$$
f(x,y)=\frac{1}{N}\sum_{u=0}^{N-1}\sum_{v=0} ^{N-1} F(u,v)e^{\frac{2\pi j}{N} (ux+vy)}
$$

幅度
$$
|F(u,v)| = \sqrt{real(F)^2+imag(F)^2}
$$
相位
$$
arctan{\frac{imag(F)}{real(F)}}
$$
对于图像的幅度谱显示，由于 |F(u,v)| 变换范围太大，一般显示 $D= log(|F(u,v)+1)$

用 `<=>` 表示傅里叶变换对
$$
f(x)<=>F(u)\\
f(x,y)<=>F(u,v)
$$

f,g,h 对应的傅里叶变换 F,G,H

$F^*$ 表示 $F$ 的共轭
## 性质
### 分离性
$$
\begin{aligned}
&F(x,v)=\sum_{y=0} ^{N-1} f(x,y)e^{\frac{-2\pi j}{N} vy}\\
&F(u,v)=\frac{1}{N}\sum_{x=0}^{N-1}F(x,v)e^{\frac{-2\pi j}{N}ux}
\end{aligned}
$$
进行多维变换时，可以依次对每一维进行变换。 下面在代码中就是这样实现的。
### 位移定理
$$
f(x,y)e^{\frac{2\pi j}{N}(u_0x+v_0y)} <=>F(u-u_0,v-v_0)
$$
$$
f(x-x_0,y-y_0)<=>F(u,v)e^{\frac{-2\pi j}{N}(ux_0+vy_0)} 
$$

### 周期性
$$
F(u,v) = F(u+N,v+N)
$$
### 共轭对称性
$$F(u,v) = F^*(-u,-v)$$
a)偶分量函数在变换中产生偶分量函数; 
b)奇分量函数在变换中产生奇分量函数; 
c)奇分量函数在变换中引入系数-j; 
d)偶分量函数在变换中不引入系数. 

### 旋转性
if $$
f(r,\theta)<=>F(\omega,\phi) 
$$
then $$f(r,\theta+t)<=>F(\omega,\phi+t)
$$
### 加法定理
1.
$$
Fourier[f+g]=Fourier[f]+Fourier[g]
$$
2.
$$
af(x,y)<=>aF[u,v]
$$

### 平均值
$$
\frac{1}{N^2}\sum_{x=0}^{N-1}\sum_{y=0} ^{N-1} f(x,y) = \frac{1}{N}F(0,0)
$$
### 相似性定理
尺度变换
$$
f(ax,by)<=>\frac{F(\frac{u}{a},\frac{v}{b})}{ab}
$$

### 卷积定理
卷积定义
1d
$$
f*g = \frac{1}{M}\sum_{m=0}^{M-1}f(m)g(x-m)
$$
2d
$$
f(x,y)*g(x,y) = \frac{1}{MN}\sum_{m=0}^{M-1}\sum_{n=0}^{N-1}f(m,n)g(x-m,y-n)
$$

卷积定理
$$
f(x,y)*g(x,y) <=> F(u,v)G(u,v)
$$
$$
f(x,y)g(x,y)<=>F(u,v)*G(u,v)
$$

离散卷积
用
$$
\sum_{i=0}^{N-1}x(iT)h[(k-i)T] <=> X(\frac{n}{NT})H(\frac{n}{NT})
$$
即两个周期为 N 的抽样函数， 他们的卷积的离散傅里叶变换等于他们的离散傅里叶变换的卷积

卷积的应用：
去除噪声， 特征增强
两个不同周期的信号卷积需要周期扩展的原因：如果直接进行傅里叶变换和乘积，会产生折叠误差(卷绕)。

### 相关定理
下面用$ \infty$ 表示相关。
相关函数描述了两个信号之间的相似性，其相关性大小有相关系数衡量

- 相关函数的定义
离散
$$f(x,y)\quad  \infty \quad g(x,y) =  \frac{1}{MN}\sum_{m=0}^{M-1}\sum_{n=0}^{N-1}f^*(m,n)g(x+m,y+n)
$$
连续
$$z(t) = \int_{-\infty}^{\infty}x^*(\tau) h(t+\tau)d\tau$$
- 定理
$$
f(x,y)\quad  \infty \quad g(x,y)<=>F^*(u,v)G(u,v)
$$
### Rayleigh 定理
能量变换
对于有限区间非零函数 f(t), 其能量为
$$
E = \int_{-\infty}^{\infty}|f(t)|^2dt
$$

其变换函数与原函数有相同的能量
$$
 \int_{-\infty}^{\infty}|f(t)|^2dt =  \int_{-\infty}^{\infty}|F(u)|^2dt
$$
## 快速傅里叶变换
由上面离散傅里叶变换的性质易知，直接计算 1维 dft 的时间复杂度维 $O(N^2)$。

利用到单位根的对称性，快速傅里叶变换可以达到 $O(nlogn)$的时间复杂度。


### 复数中的单位根
我们知道， 在复平面，复数 $cos\theta +i\ sin\theta$k可以表示成 $e^{i\theta}$， 可以对应一个向量。$\theta$即为幅角。
 在**单位圆**中 ，单位圆被分成 $\frac{2\pi}{\theta}$ 份， 由单位圆的对称性 
$$
e^{i\theta} = e^{i(\theta+2\pi)}
$$
现在记 $ n =\frac{ 2\pi }{\theta}$ ， 即被分成 n 份，幅度角为正且最小的向量称为 n 次单位向量， 记为$\omega _n$，
其余的 n-1 个向量分别为 $\omega_{n}^{2},\omega_{n}^{3},\ldots,\omega_{n}^{n}$ ，它们可以由复数之间的乘法得来 $w_{n}^{k}=w_{n}^{k-1}\cdot w_{n}^{1}\ (2 \leq k \leq n) $。
单位根的性质
1. 这个可以用 e 表示出来证明
$$
\omega_{2n}^{2k}=\omega_{n}^{k}
$$
2. 可以写成三角函数证明
$$
\omega_{n}^{k+\frac{n}{2}}=-\omega_{n}^{k} 
$$

容易看出 $w_{n}^{n}=w_{n}^{0}=1 $。

对于$ w_{n}^{k}$ , 它事实上就是 $e^{\frac{2\pi i}{n}k}$ 。
### 快速傅里叶变换的计算
下面的推导假设 $n=2^k$，以及代码实现 FFT 部分也是 如此。

利用上面的对称性，
将傅里叶计算进行奇偶分组
$$
\begin{aligned}
F(u)&=\sum_{i=0}^{n-1}\omega_n ^{iu} a^i\\
       &= \sum_{i=0}^{\frac{n}{2}-1}\omega_n ^{2iu} a^{2i}+\sum_{i=0}^{\frac{n}{2}-1}\omega_n ^{(2i+1)u} a^{2i+1}\\
      &=\sum_{i=0}^{\frac{n}{2}-1}\omega_{\frac{n}{2}} ^{iu} a^{2i}+\omega_n^u\sum_{i=0}^{\frac{n}{2}-1}\omega_{\frac{n}{2}} ^{iu} a^{2i+1}\\
      & = F_{even}(u)+\omega_n^u F_{odd}(u)
\end{aligned}
$$
$F_{even}$表示将 输入的次序中偶数点进行 Fourier 变换， $F_{odd}$ 同理，这样就形成递推公式。
现在还没有减少计算量，下面通过将分别计算的 奇项，偶项利用起来，只计算 前 $\frac{n}{2}-1$项，后面的一半可以利用此结果马上算出来。每一次可以减少一半的计算量。

对于 $\frac{n}{2}\leq i+\frac{n}{2}\leq n-1$
$$
\begin{aligned}
F(\omega_{n}^{i+\frac{n}{2}})&=F_{even}(\omega_{n}^{2i+n})+\omega_{n}^{i+\frac{n}{2}}\cdot F_{odd}(\omega_{n}^{2i+n})\\
 &=F_{even}(\omega_{\frac{n}{2}}^{i+\frac{n}{2}})+\omega_{\frac{n}{2}}^{i+\frac{n}{2}}\cdot F_{odd}(\omega_{\frac{n}{2}}^{i+\frac{n}{2}})\\
     & =F_{even}(\omega_{\frac{n}{2}}^{i})-\omega_{\frac{n}{2}}^{i}\cdot F_{odd}(\omega_{\frac{n}{2}}^{i})
\end{aligned}
$$
现在很清楚了，在每次计算 a[0..n-1] 的傅里叶变换F[0..n-1]，分别计算出奇 odd[0..n/2-1]，偶even[0..n/2-1]（可以递归地进行），
那么傅里叶变换为：
$$
F[i] = \begin{cases}
even[i]+ \omega^i \cdot odd[i], \quad i<\frac{n}{2}\\
even[i]- \omega^i \cdot odd[i], \quad else
\end{cases}
$$

## 代码
下面是 python 实现
一维用 FFT 实现， 不过 只实现了 2 的幂。/ 对于非 2 的幂，用 FFT 实现有点困难，还需要插值，所以我 用$O(n^2)$ 直接实现。

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


