class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        
        res = set()
        
        nums.sort()    
        
        for i in  range(len(nums)-1):
        
            lptr = i +1
            rptr = len(nums)-1
        
        
            while lptr<rptr:
                
                
                val= nums[i]+nums[lptr]+nums[rptr]
                
                
                if val==0:  
                    res.add((nums[i],nums[lptr],nums[rptr]))
                    lptr+=1
    
                elif val>0: rptr-=1
            
                elif val<0: lptr+=1
                    
       # print(res) 
        
        ans = []
        for tupple in res:
            ans.append(list(tupple))
            
        return ans
            