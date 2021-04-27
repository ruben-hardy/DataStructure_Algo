class Solution:
    def __init__(self):
        self.stash = {}
    
    def fib(self, n):    
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 3
        if n in self.stash.keys():
            return self.stash.get(n)
        else:
            self.stash[n] = self.fib(n-1) + self.fib(n-2))
            return self.stash.get(n)
        
        
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        return self.fib(n)


run = Solution()
print(run.climbStairs(4))