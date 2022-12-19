class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        
        dic={0:'z'}
        
        
        #asci/ord of 'a'=97, 'z'=122
        
        for i in range (97,123):
            
            dic[i-96]=chr(i)
            
     #  print(dic)
        
        
        rev_runing_sum=[0 for i in range(len(s))]
        
        r=0
        
        for i in range (len(s)-1,-1,-1):
            
            r+=shifts[i]
            rev_runing_sum[i]+=r
            
            
        #rint(rev_runing_sum)
        
        asc=[]
        for i in range(len(s)):
           
            asc.append(ord(s[i])-96)
        
        
        #rint(asc)
        res=[]
        
        
        
        for i in range(len(s)):

            
            res.append(  rev_runing_sum[i]+asc[i])
    
      # print(res)
        
        ans=""
        for i in range(len(res)):

            ans+=dic[res[i]%26]
            
        return ans
        
        
            
        
        