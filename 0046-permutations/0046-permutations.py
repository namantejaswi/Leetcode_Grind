class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        res = []
        
        def rec(curr):
            
            if len(curr)==len(nums):
                
                res.append(curr[:])
                return
            
            
            for i in nums:
                if i not in curr:
                    curr.append(i)
                    rec(curr)
                    curr.pop()
                    
        res=[]
        rec([])
        return res