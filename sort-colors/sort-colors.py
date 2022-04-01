class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Too ez gg

        indices_zeros=[]
        count=0
        indices_ones=[]
        
        for i in range(len(nums)):
            
            if nums[i]==0:
                indices_zeros.append(i)
                count+=1
                
                
        for i in range(len(nums)):
            if nums[i]!=0 and (indices_zeros):
                if indices_zeros[-1]>i:
                    nums[i],nums[indices_zeros[-1]]=nums[indices_zeros[-1]],nums[i]
                    indices_zeros.pop()
        print(nums)
            
        for i in range(len(nums)):
            if nums[i]==1:
                indices_ones.append(i)
        
        for i in range(count,len(nums)):
            if nums[i]!=1 and (indices_ones):
                if indices_ones[-1]>i:
                    nums[i],nums[indices_ones[-1]]=nums[indices_ones[-1]],nums[i]
                    indices_ones.pop()
                   
                
                