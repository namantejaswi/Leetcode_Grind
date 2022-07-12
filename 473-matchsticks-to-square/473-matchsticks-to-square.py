class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        
        #can we have 4 subsets of equal sum
        
        
        total=sum(nums)
        
        if total<4  or total%4!=0:    return False
        
        
        target=total//4
        
        nums.sort(reverse=True)
        
        @lru_cache
        def subset(l1,l2,l3,l4,idx):
            nonlocal target
            
            
            if l1==l2==l3==l4==target:  return True
        
        
            if idx>len(nums)-1: return False
            
            if l1>target or l2>target or l3>target or l4>target:
                
                return False
            
            return subset(l1+nums[idx],l2,l3,l4,idx+1) or subset(l1,l2+nums[idx],l3,l4,idx+1) or subset(l1,l2,l3+nums[idx],l4,idx+1) or subset(l1,l2,l3,l4+nums[idx],idx+1)
        
        
        return subset(0,0,0,0,0)