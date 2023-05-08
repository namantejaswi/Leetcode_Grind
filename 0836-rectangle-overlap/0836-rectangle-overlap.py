class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        
        
        #we have only 2 cordinates bottom left and top right, using that we know all 4
        #but we  can find if they overlap w/o it
        x1 =rec1[0]
        x2=rec1[2] 
        y1=rec1[1]
        y2=rec1[3]
        
        
        x3,x4=rec2[0], rec2[2]
        y3, y4 =rec2[1], rec2[3]
        
        
        #x1,y1 is the bottom left for r1 and x2,y2 the top right
        #x3,y3 is the bottom left for r2 and x4 y4 top right
        
        
        #there has to be overlap along both x and y direction in order to bbe an overall overlap
        
        
        x_overlap, y_overlap = False, False
        
        
        if max(x1,x3) < min(x2,x4):    x_overlap=True
            
        if max(y1,y3)< min(y2,y4): y_overlap=True
            
        return x_overlap and y_overlap
            
            