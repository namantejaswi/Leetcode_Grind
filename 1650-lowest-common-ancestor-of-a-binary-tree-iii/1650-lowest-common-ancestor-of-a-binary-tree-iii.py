"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        
        ptr1=p
        ptr2=q
        
        #we go upwards from p and q as long as both of them have a parent 
        
        
        
        while ptr1!=ptr2:
            
            if ptr1:
                ptr1= ptr1.parent
                
            else: ptr1=q
            
            if ptr2:
                ptr2=ptr2.parent
            else:   ptr2=p
            
               
        return ptr1
            
        
        
        