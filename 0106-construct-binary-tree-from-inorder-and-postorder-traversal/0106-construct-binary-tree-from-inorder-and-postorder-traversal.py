# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        
        #The last element of the post order is the root, since it follows l,r,root
        
        #Everything to the left of this root is going to be in the lst and everything to
        #the right will be in the rst
        
        
        if not inorder: return
        
        root = TreeNode(postorder.pop())
        
        root_index = inorder.index(root.val)        #this is why we need unique values
        
        root.right = self.buildTree(inorder[root_index+1:],postorder)
    
        
        root.left = self.buildTree(inorder[:root_index],postorder)
        
        
        
        return root