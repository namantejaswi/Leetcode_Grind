"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        #find all levels and do the appropiate change
        
        if not root: return
        bfs=[]
        q=deque()
        q.append(root)
        
        while q:
            level=[]
            
            for i in range(len(q)):
                node=q.popleft()
                level.append(node)
                
                if node.left:   q.append(node.left)
                if node.right:  q.append(node.right)
            
                
            if len(level)>0:
                
                for j in range(len(level)-1):
                    
                    level[j].next=level[j+1]
                    
                level[-1].next=None
                
        return root    