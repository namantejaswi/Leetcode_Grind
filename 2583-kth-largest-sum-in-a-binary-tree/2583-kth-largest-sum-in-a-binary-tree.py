# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        
        #We firat find the level order traversal of the entire tree
        #then we add the sum and the level index to a heap to find the kth largest in nlog k instead of n log n 
        
        
        
        bfs_order = []
        
        lvl = []
        

        q = deque([root])
        
        while q:
            
            
            for i in range(len(q)):
                
                node = q.popleft()
                lvl.append(node.val)
                
                if node.left:   q.append(node.left)
                
                if node.right:  q.append(node.right)
                    
                    
            bfs_order.append(lvl)
            lvl = []  
                
            
        heap = []
            
        for idx in range(len(bfs_order)):
            heap.append(-1*sum(bfs_order[idx]))
        
        heapq.heapify(heap)
        
        #print(heap)
        
        #print(bfs_order)
        res = []
        for i in range(k-1):
            
            if heap:    heapq.heappop(heap)
            else: return -1
        
        if heap: return -1*heap[0]     
        else: return -1
    
            
            
        
        
        
        
        