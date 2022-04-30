class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        
        freq={}
        
        
        for i in nums:
            
            if i not in freq:
                freq[i]=1
                
            else: freq[i]+=1
                
        
        
        v=freq.values()
    
        
        for i in v :
            if i%2!=0:
                return False
            
        return True