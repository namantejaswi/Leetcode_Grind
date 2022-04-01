class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        #Brute force sort the array in increasing order and return a[k-1]
        
        #nums.sort(reverse=True) 
        #return nums[k-1]
        
        
        #Now we are given k, we already know we need the kth largest elemen
        #So as soon as the number of elements in our heap exceede k
        
        #We remove the root element so by the time the number of elements 
        #in our heap exceede k that is if we are to find the 5th largest
        #element then our min heap will only have 5 elements as soon as
        #the number of elments exceede 5 we remove the root, i.e the minimum element
        #so in this way in the end we will only 5 elments or k in out heap and 
        #the root will be the smallest of the 5 largest elment i.e. 5th largest
        
        
        min_heap=[]
         
        for i in nums:#------>0(n)
            heapq.heappush(min_heap,i)#------->0(logn), it heapifies after pushing
            if(len(min_heap)>k):   #if the heap has more than k elements
                heapq.heappop(min_heap)#------->O(log n), it also heapifies after poping root
        
        return min_heap[0]#----->0(1)
    
        #Totatl time complexity using heap O(nlogn) same as sorting
        #Quicksort does this in linear time
        