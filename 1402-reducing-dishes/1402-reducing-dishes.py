class Solution:
    def maxSatisfaction(self, nums: List[int]) -> int:
        
                
        dp=[[-1]*len(nums) for i in range(len(nums))]        
        
        def calc(nums,index,length):
            
            if index>=len(nums):    return 0
            
            elif dp[index][length]!=-1: return dp[index][length]
            
                
            choose=(nums[index]*(length+1))  +  calc(nums,index+1,length+1)
            not_choose= calc(nums,index+1,length)

            dp[index][length]=max(choose,not_choose)
            return dp[index][length]
        
        
        nums.sort() #we need to sort because since we can create the dishes at any time it we take the heaviest at end
        return calc(nums,0,0)
    
    
                          
                        