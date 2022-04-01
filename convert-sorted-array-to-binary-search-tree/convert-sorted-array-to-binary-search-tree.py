# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        

        def helper(nums):
            
            if not nums:
                return
            else:
                mid=len(nums)//2
                node=TreeNode(nums[mid])
                node.left=helper(nums[:mid])
                node.right=helper(nums[mid+1:])    #mid already added

            return node
        
        return(helper(nums))

