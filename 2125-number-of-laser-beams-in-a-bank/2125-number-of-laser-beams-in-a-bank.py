class Solution:
    def numberOfBeams(self, nums: List[str]) -> int:
        
        
        ones=[]
        
        for i in nums:
            cnt=0
            for l in range(len(i)):
                if i[l]=="1":   
                    cnt+=1
                    
            ones.append(cnt)
            
            
        #print(ones)
        
        res=0
        prev=0
        
        for i in range(len(ones)):
        
            if ones[i]!=0:
                
                if prev==0:
                    prev=ones[i]
                    
                    
                elif prev!=0:
                    res+=prev*ones[i]
                    prev=ones[i]
                    
                    
        return res
                    
                    