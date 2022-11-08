class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        
        res=[]
        
        
        def calc(curr_arr,rem_arr):
            
            if not rem_arr:
                
                res.append(curr_arr)
                return res
            
            for i in range(len(rem_arr)):
                
                calc(curr_arr+[rem_arr[i]],rem_arr[:i]+rem_arr[i+1:])
                
        calc([],nums)
        return res
                
            