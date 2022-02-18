class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        
        l=int(sqrt(n)+1)
              
        list1=[]
        list2=[]
              
        #print
        for i in range(1,l):
             
            if n%i==0:
         #       print(i)
                list1.append(i)
                list2.append(n//i)
              
              
        #print(list1,list2)
        res=list1[:]+list2[::-1]
        
        #print(res)
        
        f=set()
        result=[]
        
        for i in res:
            if i not in f:
                f.add(i)
                result.append(i)
        
                
        #print(len(result),k)
        if len(result)<k:
            return -1
        
        else:   return result[k-1]