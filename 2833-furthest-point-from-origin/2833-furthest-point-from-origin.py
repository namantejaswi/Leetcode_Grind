class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        
        
        #we count l and r and there differenc is the magnitude of our diplacement from origin and we add the number of _ to it since we can move in any direction on _
        
        
        r=0
        l=0
        _=0
        
        
        for i in moves:
            
            if i =="R":  r+=1
            elif i=="L": l+=1
                
            else:   _+=1
                
        return _+abs(l-r)