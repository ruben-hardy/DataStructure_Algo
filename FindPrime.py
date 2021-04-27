class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [False] * 2 + [True] * (n-2)
        i = 2
        while i*i < n:
            if primes[i]:
                for j in range(2*i, n, i):
                    primes[j] = False
            i += 1
        return sum(primes)


                    

run = Solution()
count = run.countPrimes(4999797)
print(count)