# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        adjlist=defaultdict(list)
        self.create_graph(root,None,adjlist)
        
        q=deque([(target,0)])
        visited=set()
        
        res=[]
        
        while q:
        
            node,d=q.popleft()
            
            
            if node not in visited:     visited.add(node)
                
            else:   continue
                
            if k==d:    res.append(node.val)
                
            elif k>d:
                
                for i in adjlist[node]:
                    q.append((i,d+1))
        #print("res",res)        
        return res
        
    
    def create_graph(self,node,parent,adjlist):
        
        if not node:    return
        
        if parent:  adjlist[node].append(parent)
            
            
        if node.left:  
            
            adjlist[node].append(node.left)
            self.create_graph(node.left,node,adjlist)
                
        if node.right:
            
            adjlist[node].append(node.right)
            self.create_graph(node.right,node,adjlist)
            
    
            
            
    
        

        
        
        
        
        
        
                
                
                
                
        
        
        
        
        