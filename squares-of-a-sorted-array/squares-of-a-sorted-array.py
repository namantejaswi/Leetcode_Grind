class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        
        #Square the positive and negative arrays indivisually
        #Then merge using two pointer so we have 0(n) solution
        
        
        p=[]
        n=[]
        res=[]
        
        p= [i*i for i in nums if i>=0]
        
        n=[i*i for i in nums if i<0]
        
        
        print(p)
        print(n)
        #now the negative number we have in reverse order
        #so we start from the end and decrement the pointer
        #every time we add a number from the squared list
        
        start_ptr=0
        end_ptr=len(n)-1
        
        p_elements=len(p)
        n_elements=len(n)
        
        while(start_ptr<p_elements and end_ptr>=0): 
            
            if(p[start_ptr]>n[end_ptr]):
                res.append(n[end_ptr])
                end_ptr-=1
                
            else:
                res.append(p[start_ptr])
                start_ptr+=1
         
        print(end_ptr)
        if(end_ptr>=0):
                n_remaining=n[0:end_ptr+1]
                res.extend(sorted(n_remaining))   
        
        elif(start_ptr<p_elements):
            res.extend(p[start_ptr:])
                
        
        return res
        
        