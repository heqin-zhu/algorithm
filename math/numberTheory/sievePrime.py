def sievePrime(n):
    if n < 2:
        return 0
    prime = [1] * (n + 1)
    prime[0] = prime[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if prime[i] == 1:
            prime[i*i:n + 1:i] = [0]*len(prime[i*i:n + 1:i])
    return [i for i in range(n+1) if prime[i] == 1]


class primeSiever:
    '''sieve of Eratosthenes, It will be more efficient when judging many times'''
    primes = [2, 3, 5, 7, 11, 13]

    def isPrime(self, x):
        if x <= primes[-1]:
            return twoDivideFind(x, self.primes)
        while x > self.primes[-1]:
            left = self.primes[-1]
            right = (left+1)**2
            lst = []
            for i in range(left, right):
                for j in self.primes:
                    if i % j == 0:
                        break
                else:
                    lst.append(i)
            self.primes += lst
            return twoDivideFind(x, lst)

    def nPrime(n):
        '''return the n-th prime'''
        i = n-len(self.primes)
        last = self.primes[-1]
        for _ in range(i):
            while 1:
                last += 2
                for p in self.primes:
                    if last % p == 0:
                        break
                else:
                    self.primes.append(last)
                    break
        return self.primes[n-1]


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        n = 100
    else:
        n = int(sys.argv[1])
    ans = sievePrime(n)
    print(f'primes <= {n}, nums: {len(ans)}')
    print(ans)
