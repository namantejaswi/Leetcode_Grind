class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
            
        seats = defaultdict(set)
        
        
        for i,j in reservedSeats:
            
            #0 tells we cant seat for sure in block1 1 for block 2 and 2 for block3
            #the dictionary has key as the row number and value as the positions blocked
            if j in [2,3,4,5]:      seats[i].add(0)
            
            if j in [4,5,6,7]:      seats[i].add(1)
			
            if j in [6,7,8,9]:      seats[i].add(2)
		
        #for each blcok we sae left middle right 
        #print(seats)
        #total we can seat 2*n famlies for n rows
        #now we subtract 2 if 2 places were blocked and 1 if only one pwas blocked
        res = 2*n
		
        for i in seats:
            if len(seats[i]) == 3:  res -= 2
            else:       res -= 1
        
        return res