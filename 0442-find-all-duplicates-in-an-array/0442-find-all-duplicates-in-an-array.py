class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        
        res = []
        
        #we use the given array as a hashmap where we store the nth number at n-1 index
        #and use the -ve sign to determine if it has been seen before if so we append to our result
        
        
        
        for n in nums:
            
            if nums[abs(n)-1]<0:        #if we have seen the num before i.e. its -ve
                res.append(abs(n))      
                
                #we use abs intead of -ve because its not necessary that all intermidiate numbers b/w 1 and n are there infact its not possible, now we are only modifying the index of the number where it should be sequentially present not where it is actually, so in the later cae it can still be +ve and hence we dont multiply by -ve
                
                
                
            else:   nums[abs(n)-1]=nums[abs(n)-1]*-1
                
        #print(nums)
        return res