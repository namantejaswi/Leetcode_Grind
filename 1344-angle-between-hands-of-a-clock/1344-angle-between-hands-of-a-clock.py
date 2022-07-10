class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        
        #Eg  3:30
        
        # hour poisition 12 hours = 360 
        # 3.5 = 360/12 *3.5 =  105 
        #minute 30, 30* 360/60 = 180
        
        h=(hour + minutes/60)*30
        m=minutes * 6
        
        degree =abs(h-m)
        return min(degree,360-degree)
        
        
        
        
        
        