class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        
        adj={}
        for i in roads:
            if i[0] in adj:
                
                adj[i[0]].add(i[1])
                
            else:   adj[i[0]]={i[1]}
                
                
            if i[1] in adj:
                
                adj[i[1]].add(i[0])
                
            else:   adj[i[1]]={i[0]}
                
                 
            
        nodes=list(adj.keys())
        
        
        mx=0
        for i in (nodes):
            for j in (nodes):
                
                if i==j:    continue
                
                
                
                if j in adj[i]:
                    roads=len(adj[i])+len(adj[j])-1
                    mx=max(mx,roads)
                    
                elif j not in adj[i]:
                    mx=max(mx,(len(adj[i])+len(adj[j])))
                    
        return mx
                
            
            
            
            
            