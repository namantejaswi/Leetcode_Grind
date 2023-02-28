# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        
        
        #The problem is basically to generate all binary trees of a given tree
        
        freq = defaultdict(int)
        duplicates=[]
            
            
        def inorder(node):
        
            if not node:    return "#"
            
            
            lst = inorder(node.left)
            rst = inorder(node.right)
            
            subtree = "[" + lst + "]"+str(node.val)+"[" + rst +"]"
            
            
            freq[subtree]+=1
            
            
            if freq[subtree]==2:      #if frequency more than 2 already in in res then
                                    #or could use set and then retur list of set
                duplicates.append(node)
                     
            return subtree
            
            
        
        inorder(root)
        print(freq)
        
        return duplicates
            
            
            
            
                