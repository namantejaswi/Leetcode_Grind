class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        
    
        while tx>=sx and ty>=sy:    
            
            if tx==sx and ty==sy:   return True
            
            if tx>ty:
                
                if sy == ty:    return (tx-sx)%ty==0
                
                tx=tx%ty
                
            else:
                if sx==tx:  return (ty-sy)%tx==0
                
                ty=ty%tx
                
                
        return False        
                
        