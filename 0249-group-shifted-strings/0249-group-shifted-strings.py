class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        
        res=[]
        
        
        
        def hash_calc(s):
            
            if len(s)==1:   return 1
            
            #start index ==1
            
            hash_val=[0]*(len(s)-1)
            
            for i in range(1,len(s)):
                
                hash_val[i-1]=(ord(s[i])-ord(s[i-1]))%26
                
            return tuple(hash_val)
        
        dic={}
        
        for s in strings:
            
            h_val=hash_calc(s)
            
            if h_val in dic:
                dic[h_val].append(s)
                
            else: dic[h_val]=[s]
            
            
        return dic.values()