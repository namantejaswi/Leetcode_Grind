# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        
        #sorted in ascending order means we are given the inorder traversal of a binary
        #search tree, left root and right 
    
        #middle element will be the root of the entire tree
        #then the mid of left half will be the root of the left sub tree
        #the mid of right half will be the root of the right sub tree and so on
        
        
        
        def helper(nums):
            
            if not nums:    return 
            
            else:
                
                mid=len(nums)//2
                
                node=TreeNode(nums[mid])
                
                node.left=helper(nums[:mid])
                node.right=helper(nums[mid+1:])
                
            return node
                
        return helper(nums)
                
                
                
                
                
                
                
                
                
                