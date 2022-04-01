class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def count(nums):
            l=len(nums)-1

            #print(nums,l)
            #count(n)=max(count(n-2)+nums[i],count(n-1))
            # iteratively with memoization we can write
            # for i in (range(len(nums))) --assign---->memo[i]

            memo=[0]*len(nums)      

            if(l<0):    return 0

            elif l==0:    
                memo[0]=nums[0]

            elif(l==1):   
                memo[1]=(max(nums[0],nums[1]))

            else:
                for i in range(0,len(nums)):

                    memo[i]=max(nums[i]+memo[i-2],memo[i-1])
            return memo[l]
                         
    #Now for the case where we have cicular houses and cant select first and last
    #We calulate twice once we include from index 1 to n and then from 0 to n-1
    #sow that we can return the max of including first or including last
    
        l=len(nums)
        
        if l==1: return nums[0]     #for zero cant slice into 2 non empty halves
        
        num1=nums[0:l-1]
        #print("part 1 is",num1)
        #print(count(num1))
        num2=nums[1:l]
        #print("part 2 is ",num2)
        #print(count(num1))
        return max(count(num1),count(num2))
                
                