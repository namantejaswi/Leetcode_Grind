# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        
        q=deque()
        q.append(root)
        res=[]
        
        while len(q)>0:
            
            level=[]
            
            for i in range(len(q)):
                
                node = q.popleft()
                
                
                if node:
                    
                    level.append(node.val)
                    if node.left:   q.append(node.left)
                    if node.right:  q.append(node.right)
        
            
            res.append(level)   
        

        for i in range(len(res)):
            res[i]=sum(res[i])/len(res[i])
        
        return res
                