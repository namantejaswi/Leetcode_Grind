class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        dic={}
        
        def find(s,curr):
            if curr in dic:
                return dic[curr]
            else:
            
                if curr==len(s): return 1

                if s[curr]==0:  return 0

                res=0 
                if s[curr]!='0':
                    res+=find(s,curr+1)

                if curr+1<len(s) and (s[curr]=="1" or s[curr]=="2" and int(s[curr+1])<=6):

                    res+=find(s,curr+2)
                

                dic[curr]=res
                return res

        return find(s,0)
    