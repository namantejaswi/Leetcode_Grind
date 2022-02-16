class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        
        
        count=0
        freq=[0 for i in range(60)]
        
        for i in time:
            if i%60==0:     
                count+=freq[i%60]
            
            else:   count+=freq[60-i%60]
        
            freq[i%60]+=1
                
            
        return count
    
    
    