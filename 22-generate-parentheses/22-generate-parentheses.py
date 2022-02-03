class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res=[]
        
        def permutation(st=[]):
            
            if len(st)== 2*n:
                if isvalid(st):    
                    res.append("".join(st))
                    
                    
            else:
                
                st.append("(")
                permutation(st)
                st.pop()
                st.append(")")
                permutation(st)
                st.pop()
                
            
                
        def isvalid(s):
            count=0
            
            for i in s:
                if i=="(":  count+=1
                
                else: count-=1
                
                if count<0: return False
                
            return count==0
        
        permutation()
        return res
                    