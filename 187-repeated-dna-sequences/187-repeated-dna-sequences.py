class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        
        res=[]
        st=set()

        if len(s)<=10:
            return res
           
        lptr=0
        rptr=9
        while(rptr<len(s)):
            
            sub=s[lptr:rptr+1]
            if sub in st:
                res.append(sub)
        
            else:   st.add(sub)
            
            lptr+=1
            rptr+=1
    
        return list(set(res))
    