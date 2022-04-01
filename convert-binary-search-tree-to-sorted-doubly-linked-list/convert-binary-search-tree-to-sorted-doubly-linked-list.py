"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:

    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        previous=None
        head=None
        
        if not(root):   #if tree is empty reuturn
            return
        
        def flatten(root):
            nonlocal previous,head  #to use the nonlocal scope head and previous 
        #Base case
            if not(root):
                return
            else:
                
                #Recurssive case
                flatten(root.left)

                if previous==None:  #If we are at the end, last element of lst
                    head=root   #head is the root

                else:
                    #if we are not at the last element chnage the left to previous
                    #change the right of previous to root
                    root.left=previous
                    previous.right=root
                
                previous=root #we are out of lst set previous to root
                flatten(root.right) #call for lst


        flatten(root)   #Initial function call
        previous.right=head #circular link start and end 
        head.left=previous
        return head