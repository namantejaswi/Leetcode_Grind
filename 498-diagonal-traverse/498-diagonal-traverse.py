class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        
        #now in python by deafult we have ordered dict from 3.7
        dic={}
        
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                
                
                if i+j not in dic:
                    
                    dic[i+j]=[mat[i][j]]
                    
                else:   dic[i+j].append(mat[i][j])
                
        res=[]
        cnt=0
       # print(dic)
        for i in dic.values():
            if cnt%2==1:
                for j in i:
                    res.append(j)
            else:
                #print(i)
                for k in range(len(i)-1,-1,-1):
                    res.append(i[k])
            cnt+=1    
            
        return res