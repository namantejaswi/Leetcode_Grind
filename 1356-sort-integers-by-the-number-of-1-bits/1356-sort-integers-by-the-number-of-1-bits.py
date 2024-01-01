class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        
        
        def count_bit(n):
            
            cnt=0
            
            while(n):
                n = n & n-1     
                #The rightmost non zero bit will always become zero on  when we and with n-1 and we do this till n becomess 0, the number of times we have to eliminate 1 bit  is the total number of 1 bit 
            
            
                cnt+=1
                
            return cnt
        
        
        res =[]
        
        for i in arr:
            
            res.append([i,count_bit(i)])
           
        res.sort(key = lambda x:(x[1],x[0])) #for keeping smaller number for same 1 bit
        
        #print(res)
        ans=[]
        
        for v in res:
            ans.append(v[0])
            
        return ans