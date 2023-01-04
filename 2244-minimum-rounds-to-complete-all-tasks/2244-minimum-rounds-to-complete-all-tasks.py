class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
        
        
        #3k , 3k+1, 3k+2
        
        #for 1 we cant do nothing
        #for 3k +1   
        # 3k+1  =  3(k-1)  +2k
        
        freq=dict(Counter(tasks))
        
        cnt=0
        print(freq)
        for k,v in freq.items():
            
            if v==1: return -1
            
            elif v%3==0:  cnt+=v//3
                
            elif v%3==1:  
                
                q=v//3
                
                cnt=cnt+ q+1
            
              
            elif v%3==2:
                
                print(v)
                
                cnt=cnt+(v//3)+1
                
                
        return cnt
            
            
      