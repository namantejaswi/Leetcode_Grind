class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        
    #Sort the interval by earliest finish time
    
        
        s_inter=sorted(intervals, key =lambda i:i[1])
    
        print(s_inter)
        
        flag=True
      
    
        for i in range(0,len(s_inter)-1):
            
            if s_inter[i][1]>s_inter[i+1][0]:
                flag=False
            
            
        return flag