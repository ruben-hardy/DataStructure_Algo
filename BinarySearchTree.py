class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        mid = len(nums)//2
        root = TreeNode()
        if mid==0:
            return
        root.val = nums[mid]
        root.left = self.sortedArrayToBST(nums[0:mid-1])
        root.right = self.sortedArrayToBST(nums[mid+1:len(nums)-1])
        return root


run = Solution()

print(run.sortedArrayToBST([-10, -3, 0, 5, 9]))