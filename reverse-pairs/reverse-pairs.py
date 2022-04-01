class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        count_inversion=0

        def divide(arr):            
            if len(arr)==1:
                return arr
            else:
                mid=len(arr)//2
                left=divide(arr[:mid])
                right=divide(arr[mid:])
                return(merge(left,right))
            
        def merge(left,right):
            
            nonlocal count_inversion
            s1=len(left)
            s2=len(right)
            ptr1=ptr2=0
            
            while(ptr1<s1 and ptr2<s2):
                
                if(left[ptr1]>2*right[ptr2]):        
                    count_inversion+=len(left)-ptr1
                    #count_inversion+=len(left[ptr1:]) 
                    ptr2+=1
                
                #if soome element of left at ptr1  is greater than twice of some                     #element in right at ptr2 then it is given that all in left which
                #come after ptr1 will also be greater than that elment in right
                #as the arrays after merging are sorted.
                
                #Thus the number of inversions we can see is this element in left
                #and the remaining number of elments
                else:
                    ptr1+=1
                    
            
            #if 
            
            return sorted(left+right)
        divide(nums)
        return count_inversion
    
                
            
            
            
            
            