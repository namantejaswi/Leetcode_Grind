class Solution:
    def countBits(self, n: int) -> List[int]:
        
        
        
        #Binary Representation  Number of ones  
        # 0         0000        0
        # 1         0001        1
        # 2         0010        1
        # 3         0011        2
        # 4         0100        1 
        # 5         0101        2
        # 6         0110        2
        # 7         0111        3 
        # 8         1000        1
        # 9         1001        2
        # 10        1010        2
        
        #now even numbers will always have the same number of ones as even/2 that is
        # 4,8,16   wil have 1 one as 2
        # 3,6,12  will have 2 ones as 3
        # 5,10,20 will have 2 ones and so on
        
        
        #this because when the factor of a number increases by 2 we are essentially
        # shifting the bits by one to the left i.e perfroming  left shift << to double
        
        
        
        # so we know that when we are performing left shift the bits remain same only the position i.e. significance changes that is how we can relate the subproblem
        
        #Now for odd number we know every odd number x = 2y+1 where y is an even number so  even number will have right most bit zero then the odd number x is simple the binary represenation of 2y with right bit flipped i.e 1 . 
        
        #So n and n/2 will have same bits just shiftedd if n is even and if n is odf n//2 plus one right bit
        
        # for even number n number_of_one_bits(n) = number_of_one_bits(n/2)
        # for oddd number number_of_one_bits(n) = number_of_one_bits(n//2) + 1
        
        #now we have the sub problem relation so it is very easy to solve using the base condition for n =0 and n=1 and building bottom up or solving recurssively with caching.
        
        '''
        if n==0:    return [n]
        if n==1: return[0,1]
        res = []
        dp = [-1 for i in range(n+1)]
        dp[0],dp[1] = 0,1
        
        def calc(n):
            
            if dp[n]!=-1:   return dp[n]
        
            elif n%2==0:
                
                dp[i]=calc(int(n/2))  #even number will have the same number of ones
                return dp[i]
            
            else:  
                if dp[i]!= -1: return dp[i]
                
                else:
                    dp[i]=calc(int(n//2))+1
                    return dp[i]
                    
        for i in range(n+1):
            
            res.append(calc(i))
                       
        return res
    '''
        
        dp = [-1 for i in range(n+1)]
        if n==0:    return [0]
        
        dp[0],dp[1] = 0,1
        
        
        for i in range(2,n+1):
            
    
            if i%2==0: dp[i] = dp[int(i/2)]
                
            else:  dp[i] = dp[int(i//2)]+1
                    
                            
                
        return dp
        
        
        
        
        
        