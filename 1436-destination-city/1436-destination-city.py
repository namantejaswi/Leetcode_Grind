class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        outdegree= set()
        
        #we store cities which have an outddegree
        
        
        for travel in paths:
            if travel[0] not in outdegree:
                outdegree.add(travel[0])
                
        for cities in paths:
            if cities[1] not in outdegree: return cities[1]
            