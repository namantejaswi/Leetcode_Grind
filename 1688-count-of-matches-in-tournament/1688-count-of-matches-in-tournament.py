class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        def teams(n):
            
            
            if n==2:
                return 1
           
            
            elif n%2==0:
                return n/2+teams(n/2)
            
            elif n%2==1:
                return (n-1)/2 + teams(((n-1)/2)+1)
            
        if n==1: return 0 #the fuck will you play with 1 team gg input

        return teams(n)