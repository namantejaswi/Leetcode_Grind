class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        m=math.floor(len(nums)/2)
        
       
        #using boyer moore algorithm
        
        #Key idea is majority element occurs more than half the number of items
        #so we count elements and assign them to candidate if fe find same +1
        #if different -1 since the majority element occurs more than half the no.
        #of items in the end we must have the candidate as the majority element
        
        count=0
        candidate=None
        
        for i in nums:
            
            if count==0:
                candidate=i
                count+=1
                
            elif candidate==i:
                count+=1
            else:
                count-=1
                
        return candidate