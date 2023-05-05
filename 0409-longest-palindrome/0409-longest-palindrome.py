class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        res=0
        dic = dict(Counter(s))
        flag=True
        for k,v in dic.items():
            
            if v%2==0:  res+=v
                
            if v%2==1:
                
                if flag:    
                    res+=v
                    flag=False
                elif not flag:    res+=v-1
                    
                    
        return res
                    
        
        
#         dic = dict(Counter(s))
        
        
#         even =dict()
#         odd=dict()
        
        
#         for i in dic.items():
            
#             if i[1]%2==0:
                
#                 even[i[0]]=i[1]
                
#             else:   odd[i[0]]=i[1]
                
        
#         #print(even,odd)
        
#         res = 0
        
#         if even:    res+=sum(even.values())
            
#         mx=0
        
#         max_key=None
        
#         for key,val in odd.items():
            
#             if val>mx:
#                 mx=val
#                 max_key=key
                
#         res+=mx
    
#         if max_key:del(odd[max_key])
            
            
#         for key,val in odd.items():
            
#             res+=val-1
            
#         return res
            
        
        
        