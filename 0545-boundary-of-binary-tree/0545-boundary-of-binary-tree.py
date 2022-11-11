# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        
        left_boundary=[root]        
        node=root.left
        
        while node:
            left_boundary.append(node)
            if node.left:   node=node.left
            else:   node=node.right
                
        
        right_boundary=[]
        node=root.right
        
        while node:            
            right_boundary.append(node)
            
            if node.right:  node=node.right
            else:   node=node.left
                
        #use bfs or dfs to find leaves
        #find leaves using dfs,
        leaf=[]
        
        stack=[root]
        
        while stack:
            node=stack.pop()
            
            if node.left:   stack.append(node.left)
            if node.right:  stack.append(node.right) 
            elif not node.left and not node.right:  leaf.append(node)
            
        #print(leaf)
                        
        res=[]
        visited=set()
        
        for node in left_boundary:
            
            if node not in visited:
                res.append(node.val)
                visited.add(node)
                
        for node in reversed(leaf):
            if node not in visited:   
                res.append(node.val)
                visited.add(node)
                
        for node in reversed(right_boundary):
            if node not in visited:   
                res.append(node.val)
                visited.add(node)
                
        return res
                
                
        
        
        
        
        
        
        
        
        
        
           