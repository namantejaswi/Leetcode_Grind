class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
    #The number of ways to arrange n objects in a row, of which exactly p objects are identical, is n!/p!
    
    #we start at 1,1 insteadd of 0,0 so we have r-1 choices and c-1 choices to move own or right
    
        return int((factorial(m+n-2))/(factorial(m-1)*factorial(n-1)))