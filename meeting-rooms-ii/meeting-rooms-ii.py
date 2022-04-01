class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        #Sexy sawal
        
        #number of rooms required is the same as the max concurrent overlap
        
        start=[]
        end=[]
                
        
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        
                
        start.sort()
        end.sort()
        print(start,end)
        
        k=len(intervals)   #every meeting which starts must end
        st_ptr=0
        en_ptr=0
        
        max_count=0
        count=0
        while(st_ptr!=k or en_ptr!=k):
            if(start[st_ptr]<end[en_ptr]):
                count+=1
                max_count=max(count,max_count)
                st_ptr+=1
                
            else:
                count+=-1
                en_ptr+=1
            
            if(st_ptr==k):  return max_count        #only end times left
            
        return max_count
        