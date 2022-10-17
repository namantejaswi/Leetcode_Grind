# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        
        bfs=[]
        
        
        q=deque()
        q.append(root)
        
        
        while q:
            lvl=[]
            
            for i in range(len(q)):
            
                v=q.popleft()
                
                lvl.append(v.val)
                
                if v.left:  q.append(v.left)
                if v.right: q.append(v.right)
                
                
            if lvl:
                bfs.append(lvl)
                
        return sum(bfs[-1])
            