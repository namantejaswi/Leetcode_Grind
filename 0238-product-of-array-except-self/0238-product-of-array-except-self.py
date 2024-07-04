class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
            
            
        zero_count = 0
        prod= 1
        non_zero_prod = 1
        res=[]

        for i in nums:
            prod = prod*i
            if i ==0: 
                zero_count +=1
                if zero_count>1:    return [0]*len(nums)

            else: non_zero_prod = non_zero_prod*i

                
        for i in nums:

            if i == 0: res.append(non_zero_prod)

            else:   res.append(prod//i)
        print(res)
        return res
