class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        
        
        dic={}
        
        for i in mat:
            for j in range(len(i)):
                if i[j] not in dic:
                    dic[i[j]]=1
                    
                else:   dic[i[j]]+=1
                    
                    
        for k,v in dic.items():
        
            if v==len(mat):
                return k
            
        return -1