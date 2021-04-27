class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0
        for i in nums:
            temp = max(i + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

            


run = Solution()
result = run.rob([3, 1, 1, 3])
print(result)
#9 7 3 2 1
#2 1 3 0 4 

