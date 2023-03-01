class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        
        #Merge sort nlogn
            
            
        def merge(arr_1,arr_2):
            
            res=[]
            ptr_1, ptr_2 = 0,0
            
            while ptr_1<=len(arr_1)-1 and ptr_2<=len(arr_2)-1:
                
                if arr_1[ptr_1]<arr_2[ptr_2]:
                    
                    res.append(arr_1[ptr_1])
                    ptr_1+=1
                    
                else:
                    res.append(arr_2[ptr_2])
                    ptr_2+=1
                    
            if ptr_1!= len(arr_1):
                res.extend(arr_1[ptr_1:])
            
            else:   res.extend(arr_2[ptr_2:])
            
            
            return res
        
            
        def merge_sort(arr):
            
            if len(arr)==1:     return arr
            
            else: 
                
                mid = len(arr)//2
                
                left=merge_sort(arr[:mid])
                right=merge_sort(arr[mid:])
                
                #merged= merge(left,right)
                
                #print("left",left,"right",right,"arr returning after merge",merged)
                
                return merge(left,right)
                
                
        return merge_sort(nums)
                
            
            
        
            
            
            
        