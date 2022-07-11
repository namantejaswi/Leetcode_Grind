# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        
        #We are to do a level order order traversal and find the rightmost element
        
        
        #bfs_order=[]
        q=deque()
        q.append(root)
        right_side_view=[]
        
        while len(q)>0:
            
            level=[]
            
            for i in range(len(q)):
                
                v=q.popleft()
                
                if v:
                    level.append(v.val)
                    q.append(v.left)
                    q.append(v.right)
                    
            if level:
                #bfs_order.append(level)
                right_side_view.append(level[-1])
                
        return right_side_view