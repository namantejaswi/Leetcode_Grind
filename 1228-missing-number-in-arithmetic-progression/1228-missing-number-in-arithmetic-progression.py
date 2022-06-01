class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        
        
        d=min(arr[1]-arr[0],arr[2]-arr[1])
        
        n=len(arr)+1
        
        s=sum(arr)
        mi=min(arr)
        mx=max(arr)
        
        return int(n*((mx+mi)/2)-sum(arr))