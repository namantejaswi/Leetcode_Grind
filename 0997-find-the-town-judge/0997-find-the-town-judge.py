class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        
        indegree = [[] for i in range(n+1)]
        outdegree= [[] for i in range(n+1)]
        
        
        for elem in trust:
        
                        
            outdegree[elem[0]].append(elem[1])    
            indegree[elem[1]].append(elem[0])
            
            
            
        potential=[]
        for i in range(1,len(indegree)):
            
            if len(indegree[i])==n-1:   potential.append(i)
      
    
        for i in potential:
            if len(outdegree[i])==0: return  i
        
        
        return -1
        
        