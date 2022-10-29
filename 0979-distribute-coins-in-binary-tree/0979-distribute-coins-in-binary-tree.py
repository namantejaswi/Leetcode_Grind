# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        
        count=0
        
        #take 1 and give remaining to childreen
        
        def dfs(node):
            nonlocal count
            if not node:    return 0
            
            coins_on_lst = dfs(node.left)
            coins_on_rst = dfs(node.right)
            
            count+=abs(coins_on_lst)+abs(coins_on_rst)
            
            return node.val+coins_on_rst+coins_on_lst-1
        
        
        dfs(root)
        return count