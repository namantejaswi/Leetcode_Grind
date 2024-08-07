# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:    return 
        res = []
        
        
        q = deque([root])
        
        
        while q:
            
            level = []
            
            for i in range(len(q)):
                
                node = q.popleft()
                
                level.append(node.val) 

                
                if node.left:   q.append(node.left)
                    
                if node.right:  q.append(node.right)
                    
            res.append(level)
            
            
        ans=[]
        for l in res:
             ans.append(l[-1])
                
        return ans
                 
            