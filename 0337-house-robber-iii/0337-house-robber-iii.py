# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        
        dic={}
        def calc(node):
            
            if not node:    return 0
            
            if node in dic: return dic[node]    
        
            pick = node.val
            
            #if we pick we cant pick the next 2 childs but then we pick all the 4 grand childreen 
            
            if node.left :
                if node.left.left:  pick+=calc(node.left.left)
                if node.left.right: pick+=calc(node.left.right)
                
            if node.right :
                if node.right.left: pick+=calc(node.right.left)
                if node.right.right:    pick+=calc(node.right.right)
                
            
            dont_pick = calc(node.left) + calc(node.right)
            
            dic[node]= max(pick,dont_pick)  
            return dic[node]
        
        return calc(root)
        