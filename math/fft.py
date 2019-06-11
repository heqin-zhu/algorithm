import numpy as np


def _fft(a, invert=False):
    '''fft,   len(a) is power of two'''
    N = len(a)
    if N == 1:
        return [a[0]]
    else:
        even = _fft(a[::2], invert)
        odd = _fft(a[1::2], invert)
        i = 2j if invert else -2j
        factor = np.exp(i * np.pi * np.arange(N // 2) / N)
        prod = factor * odd
        return np.concatenate([even + prod, even - prod])


def fft(a):
    '''fourier[a]'''
    n = len(a)
    if n == 0 or n&(n-1)!=0:
        raise Exception(f"[Error]: {n} is not power of 2")
    return _fft(a)


def ifft(a):
    '''invert fourier[a]'''
    n = len(a)
    if n == 0 or n&(n-1)!=0:
        raise Exception(f"[Error]: {n} is not power of 2")
    return _fft(a, True) / n


def fft2(arr):
    return np.apply_along_axis(fft, 0, np.apply_along_axis(fft, 1, np.asarray(arr)))


def ifft2(arr):
    return np.apply_along_axis(ifft, 0, np.apply_along_axis(ifft, 1, np.asarray(arr)))


def test(n=128):
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
    test(128)
