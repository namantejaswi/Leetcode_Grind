# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        #find the level order traversal and first element of last level
        
        
        bfs=[]
        
        q=deque()
        q.append(root)
        
        while q:
            
            level=[]
            
            for i in range(len(q)):
                
                v=q.popleft()
                level.append(v.val)
                if v.left:  q.append(v.left)
                if v.right: q.append(v.right)
                    
                    
            if level:
                bfs.append(level)
    
        return bfs[-1][0]
                