# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        
        if not root:    return
        
        bfs = []
        q = deque([root])
        
        
        lvl = []
        
        
        while q:
            
            for i in range(len(q)):
                
                node = q.popleft()
                
                lvl.append(node.val)
                
                if node.left:   q.append(node.left)
                    
                if node.right:  q.append(node.right)
                    
                    
            bfs.append(lvl)
            lvl=[]
            
        arr = []
        
        for idx in range(len(bfs)):
            
            arr.append([sum(bfs[idx]),idx])
      
        res=None
        mx=float("-inf")
        for s,i in arr:
            if s>mx:    
                mx = s
                res = i
                
        return res+1
        
        
        
        
            