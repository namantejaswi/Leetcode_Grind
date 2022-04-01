class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        
        #The key idea is we know that we use a set to check if each element
        #is the starting of a sequence if for element i, i-1 does not exist in set
        #then check if i+1 exists in set using a while loop
        #Now this while loop will maximum run for n times as it will enter only on
        #the condition i-1 does not exist 
        
        #eg- sat 1,2,3,4,7,8,9, 20,21,22,23,24,25,26 
        #the while loop will only be for 1,7,20 now for all of them combined
        #the loop can't run more than n times as n is the total number of elments
        
        
        n_set=set(nums)
        max_seq=0
        
        
        for i in n_set:#instead of checking in nums we can check n_set to reduce time
            
            j=i
            
            if j-1 not in n_set:
                seq=0
                while(j+seq in n_set):  
                    seq+=1              
                    max_seq=max(max_seq,seq)
                #print("seq",seq)
        #print(seq)       
        return max_seq
                #print("start",j)
            