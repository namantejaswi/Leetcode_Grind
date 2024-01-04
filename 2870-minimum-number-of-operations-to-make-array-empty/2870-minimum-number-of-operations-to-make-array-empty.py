class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        
        freq={}
        
        for i in nums:
            
            if i in freq:   freq[i]+=1
                
            else:   freq[i]=1
                
                
        cnt=0 
        
        
        #also 3,4,5,6 any number is represented by some val of 3x+2y
                
        for k,v in freq.items():
            
            if v==1:    return -1
            if v%3==0:  cnt+=v/3
                
            elif v%3==1:  
                
            
                #7 2*2 +3*1
                #10 2*2 +3*2
                #13 2*2 + 3*3
                #16  2*2 + 3*4
                
                cnt=cnt+2
                v=v-2*2
                cnt+=v/3
                
            elif v%3==2:
                
                #5  2*1 + 3*1
                #8  2*1 + 3*2
                #11  2*1 + 3*3
                
                cnt+=1
                v=v-2
                cnt+=v/3
                
                
                
                
        return int(cnt)
                
                
                
                
            
            