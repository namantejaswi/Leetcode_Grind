class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        
        
        #optimize value assignment
        #sort by degree and greedy  assignment
        
        
        deg = defaultdict(set)
        
        for edge in roads:
            deg[edge[0]].add(edge[1])
            deg[edge[1]].add(edge[0])
            
        index_score = {}
        for i in range(n):
            index_score[i] = len(deg[i])
         
        #can use heap for better eficiency
        sorted_index_score = dict(sorted(index_score.items(), key=lambda x: x[1], reverse=True))
        
        #print(sorted_index_score)
        
        
        for k, v in sorted_index_score.items():
            
            sorted_index_score[k]=n
            n=n-1
            
        #print(sorted_index_score)
        
        
        total = 0 
        
        for e in roads:
            total += sorted_index_score[e[0]]+sorted_index_score[e[1]]
            
            
        return total