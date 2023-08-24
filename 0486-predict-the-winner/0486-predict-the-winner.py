class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        
        l  = len(nums)
        
        
        dp = dict()
        
        def max_score(l,r):
            
            
            if (l,r) in  dp :   return dp[(l,r)]
            
            if l == r:  return nums[l] #we have no choidce only one element left
            
            
            #we subtract so that we can at the endd check if the difference is +ve 
            #also since player 1 moves first 
            choose_left = nums[l] - max_score(l+1,r)
            choose_right = nums[r] - max_score(l,r-1)
            
            dp[(l,r)] =  max(choose_left,choose_right)
            return dp[(l,r)]
            
        return (max_score(0,l-1)>=0)