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
            
        heap = []
        
        for idx in range(len(bfs)):
            
            heap.append([-1*sum(bfs[idx]),idx])
            
            
        heapq.heapify(heap)
        
        return heap[0][1]+1
            