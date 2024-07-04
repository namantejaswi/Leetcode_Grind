class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        
        #represent max,min prod ending at curr index
        max_prod = 1
        min_prod = 1
        mx=0
        flag = 0    #to see if we only have a single negative i.e ensure at  least 1+ve or 2 consequetive -ve at the very least
        
        if len(nums)==1: return nums[0]
        
        for i in range(len(nums)):
            
            if nums[i] == 0: 
                
                max_prod , min_prod = 1,1
            
            elif nums[i] >0:
                flag=1
                max_prod = max(max_prod*nums[i],nums[i])
                
                min_prod = min_prod*nums[i]
            
                mx = max(mx,max_prod)
            
            elif nums[i]<0:
                
                mi = min_prod #temp var
                
                min_prod = min(max_prod*nums[i],1)
                
                max_prod = max(mi*nums[i],1)
                
                mx = max(mx,max_prod)
                
                if mi*nums[i] >0: flag=1
        print(flag)          
        if flag==0 : return  0
        if flag==0: return max(nums)
        return mx
                   
        