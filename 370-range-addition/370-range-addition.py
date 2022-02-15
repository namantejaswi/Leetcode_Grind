class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        
        arr=[0  for i in range(length)]
        prefix_sum=0
                
        for i in range(len(updates)):
    
           
            start=updates[i][0]
            end=updates[i][1]
            increment=updates[i][2]
            
            
            arr[start]+=increment
            
            if end+1<len(arr):
                arr[end+1]-=increment
                
                
        for i in range(0,len(arr)):
            
            prefix_sum+=arr[i]
            arr[i]=prefix_sum
            
            
        return arr