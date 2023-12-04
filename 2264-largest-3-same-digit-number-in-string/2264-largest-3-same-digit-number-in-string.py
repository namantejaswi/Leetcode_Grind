class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        mx = -1
        
        for i in range(len(num)-2):
            
            if num[i]==num[i+1] and num[i+1]==num[i+2]:
                
                mx = max (mx, int(num[i]))
                
                
        return str(mx)*3 if mx!=-1 else ""
        