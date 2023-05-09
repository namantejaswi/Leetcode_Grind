class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        
        #Overlap area = x overlap * y overlap
        
        x_overlap = 0
        y_overlap = 0
        
        
        
        #x overlap if max of start point less than min of end point
    
        
        if max(ax1,bx1)< min(ax2,bx2):  x_overlap = min(ax2,bx2)-max(ax1,bx1)
            
            
            
        if max(ay1,by1)<min(ay2,by2):   y_overlap = min(ay2,by2)- max(ay1,by1)
            
        area_a = (ay2 - ay1) * (ax2 - ax1)
        area_b = (by2 - by1) * (bx2 - bx1)
            
        return area_a+area_b -(x_overlap*y_overlap)