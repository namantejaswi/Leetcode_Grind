class Solution:
    def maximumSwap(self, num: int) -> int:
        
        #Key Idea the larger number should be towards the 0 index
        
        num = [int(d) for d in str(num)]
        
        mx_pos=len(num)-1
        
        p1,p2=0,0        #The positions we swap
        
        for i in range(len(num)-1,-1,-1):
            if num[i]>num[mx_pos]:
                mx_pos=i
                
            # if we find a smaller number while going left we swap it with max
            #since the loop runs from back we eventually swap with the left most smaller no.
            
            elif num[i]<num[mx_pos]:    
                p1=i
                p2=mx_pos
        
        num[p1],num[p2]=num[p2],num[p1]
        
        #print(num)
        
        res=0
        p=0
        
        for i in range(len(num)-1,-1,-1):
            res+=num[i]*(10**p)
            p+=1
            
        return res
        

        
        
        
        
        
    
        
        
        
        
        
        