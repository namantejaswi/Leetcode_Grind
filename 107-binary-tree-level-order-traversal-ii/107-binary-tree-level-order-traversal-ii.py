# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        lvl_order=[]
        
        q=deque()
        
        if root:    q.append(root)
        
        
        while len(q)>0:
            
            levels=[]
            for i in range(len(q)):
                
                node=q.popleft()
                
                if node:
                    
                    levels.append(node.val)
                    if node.left:   q.append(node.left)
                    if node.right:  q.append(node.right)
                    
                        
                        
            lvl_order.append(levels)
        
        return lvl_order[::-1]
        
        
        
        
        
        
        
        
        
        
        
        
        