# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        
        res=[]
        min_word=None
        
        def root_to_path(node,path):
            
            nonlocal min_word
            if not node:    return    
            
            else:
                
                if not node.left and not node.right:
                    
                    path+=chr(node.val+97)
                    v=(path[::-1])
                    res.append(v)
                    if not min_word:    min_word=v
                    else: min_word=min(min_word,v)
                    
                else:
                    root_to_path(node.left,path+chr(node.val+97))
                    root_to_path(node.right,path+chr(node.val+97))
                    
        root_to_path(root,"")
        #print(res)
        
        return min_word
        
        
                
        