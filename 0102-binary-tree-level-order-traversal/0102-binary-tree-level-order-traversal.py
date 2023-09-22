# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        if not root:    return
        bfs_order = []
        
        lvl = []
        
        q = deque([root])
        
        
        while q:
            
            
            for i in range(len(q)):
                
                node = q.popleft()
                lvl.append(node.val)
                
                
                
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                
            
            if lvl:     
                bfs_order.append(lvl)
                lvl = []
                            
        return bfs_order
            