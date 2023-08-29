class Solution:
    def bestClosingTime(self, nums: str) -> int:
        
          
        
        #for an array nums of lenght l we have l+1 options of our closing time including the point 0 i.e we dont even open
        
        
        cnt = 0
        for i in nums:  
            if i=="Y":  cnt+=1
        
        
        curr_p = min_p = cnt
        t=0
        
        for i,ch in enumerate(nums):
            
            if ch=="Y": curr_p -=1
                
            else:   curr_p+=1
                
            if curr_p<min_p:
                
                min_p=curr_p
                t = i+1
                
                
        return t
                
        
        
        
            
        
            
            