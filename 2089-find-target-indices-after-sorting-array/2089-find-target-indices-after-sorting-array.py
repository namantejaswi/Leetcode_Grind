class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        
        #Trivial soln nlogn
        
        
        count=0
        greater=0
        lesser=0
        
        for i in nums:
            if i == target:
                count+=1
                
            elif i > target:
                greater+=1
                
            elif i < target:
                lesser+=1
                
        
        #lower_bound = lesser 
        #upper_bound = lesser + count -1 
        #print(lower_bound,upper_bound)
        
        res=[]
        for i in range(lesser, lesser + count ):
             res.append(i)
                
        return res
        
                
                
        
                
    