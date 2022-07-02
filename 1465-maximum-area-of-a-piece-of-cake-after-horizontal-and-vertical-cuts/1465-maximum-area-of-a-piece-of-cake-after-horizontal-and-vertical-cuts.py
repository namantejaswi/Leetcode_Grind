class Solution:
    def maxArea(self, y: int, x: int, h: List[int], w: List[int]) -> int:
        
        h.sort()
        w.sort()
        
        mx_delta_y=max(h[0],y-h[-1])
        mx_delta_x=max(w[0],x-w[-1])
        
    
        for i in range(1,len(h)):
            
            mx_delta_y=max(mx_delta_y,h[i]-h[i-1])
            
        for i in range(1,len(w)):
            
            mx_delta_x=max(mx_delta_x,w[i]-w[i-1])
            
            
    
        return (mx_delta_y*mx_delta_x)%(10**9 + 7)