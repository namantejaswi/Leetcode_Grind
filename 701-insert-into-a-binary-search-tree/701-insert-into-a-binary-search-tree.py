# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        
        if not root:    #If we reach null we create a new node and return it
            return TreeNode(val)
        
        if      root.val>val:  #if val greater than current node search in lst
                root.left=self.insertIntoBST(root.left,val)
                
                #else search in rst
        else:   root.right=self.insertIntoBST(root.right,val)
            
                #once we find and empty node we insert
        return root