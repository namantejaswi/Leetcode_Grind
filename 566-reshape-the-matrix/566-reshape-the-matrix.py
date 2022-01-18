class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        
        
        #covert the orignal list into a 1d and then add element as you
        #iterate through second list
        
        
        arr=[]
     
        res = [ [ 0 for i in range(c) ] for j in range(r) ]
        
        
        #print(res)
        count=0
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                arr.append(mat[i][j])
        
        if len(arr)!=r*c:   return mat
        
        for i in range(r):
            for j in range(c):
                
                (res[i][j])=arr[count]
                count+=1
        return res