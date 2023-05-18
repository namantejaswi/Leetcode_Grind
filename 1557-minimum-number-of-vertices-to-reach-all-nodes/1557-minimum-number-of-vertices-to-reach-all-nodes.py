class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        
        
        indegree = [ set() for i in range(n)]
        
        for e in edges:
            
            indegree[e[1]].add(e[0])
            
            
            
        res=[]
        for i in range(len(indegree)):
            
            if (len(indegree[i]))==0:   res.append(i)
                
        return res
            