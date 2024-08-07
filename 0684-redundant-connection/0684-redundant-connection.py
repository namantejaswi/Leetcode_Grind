class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        
        #All nodes should be still reachable we need to reduce the graph to a tree
        #n nodes will be reachable by n-1 edges
        #n nodes n-1 edges
        
        
        #0 wont be used 1-n nodes
        parent = [ i for i in range(len(edges)+1)]
        
        def find(n):
            
            if parent[n]!=n:
                
                return find(parent[n])
            
            else:   return parent[n]
        
        
        def union(x,y):
            
            p_x, p_y = find(x), find(y) 
            
            if p_x == p_y:  return True
            
            else: 
                
                parent[p_x] = p_y
                return False
            
            
        #now we union all edges and return the edge where both have same parent
        
        for x,y in edges:
            if union(x,y):  return[x,y]