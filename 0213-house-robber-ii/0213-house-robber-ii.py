class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #we calculate by taking 2 inputs 1st from 0 to n-1 and then from 1 to n
        
        
        if len(nums)<=2:return max(nums)
        
        def calc(houses):
        
            dp=[-1 for i in range(len(houses))]
            dp[0]=houses[0]
            dp[1]=max(houses[0],houses[1])
            
            def count(index):
            
                
                if index<0: return 0# will never actually be here 
                
                if dp[index]!=-1:   return dp[index]
                
                
                else:
                    
                    pick= count(index-2)+houses[index]
                    no_pick=count(index-1)
                    
                    dp[index]=max(pick,no_pick)
                    
                    return dp[index]
            
            count(len(houses)-1)
            return dp[-1]
                   
        
        nums2=nums[1:]
        nums.pop()    
        return max(calc(nums[:]), calc(nums2[:]))         