# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        stack = [ i for i in range(n)]
        
        while len(stack)>1:
            
            element_1 = stack.pop()
            element_2 = stack.pop()
            
            
            if knows(element_1,element_2):stack.append(element_2)
                
                
            elif knows(element_2,element_1):stack.append(element_1)
                
        
        #we have our potential celibrity, we check if everbody knows him and he knows none 
        if not stack:   return -1  # 2 elements that know each other
        potential_celeb = stack[0]
        
        for i in range(n):
            
            if i == potential_celeb:    continue
                
                
            elif knows(i,potential_celeb) and not knows(potential_celeb,i):  continue
                
            else:   return -1
            
        return potential_celeb