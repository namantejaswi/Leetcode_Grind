class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        
        l=0
        r=0
        s=set()
        mx=0
        summation=0
        
        for r in range(len(nums)):
           # print(summation,"left",l,"right",r)
            
            if nums[r] not in s:
                s.add(nums[r])
                summation+=nums[r]
                #print("adding",nums[r])
            else:
                summation+=nums[r]
                while(l<r):
                    if nums[l]!=nums[r]:
                        s.remove(nums[l])
                        summation-=nums[l]
                        #print("subtracting",nums[l])
                        l+=1
                           
                    elif nums[l]==nums[r]:
                        summation-=nums[l]
                       # print("subtracting",nums[l])
                        l+=1
                        break                        
            
            #print(summation)
            mx=max(mx,summation)           
                
        return mx
            