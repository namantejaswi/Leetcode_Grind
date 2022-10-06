# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        
        q=deque()
        q.append(root)
        res=[]
        
        while len(q)>0:
            
            level=[]
            
            
            for i in range(len(q)):
                
                
                v=q.popleft()
                
                
                if v:
                    level.append(v.val)
                    q.append(v.left)
                    q.append(v.right)
                    
                    
            if level:
                res.append(max(level))
                
        return res
                    
                    
            
            