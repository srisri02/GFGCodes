class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	list=[]
    	for i in range(0,n):
    	    for j in range(i+1,n):
    	        if arr[j]==arr[i]:
    	            if arr[i] not in list:
    	                list.append(arr[i])
    	list.sort()
    	if not list:
    	    list=[-1]
    	return list
    	 
    	            


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends




Given an array a[] of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than once in the given array. Return the answer in ascending order.

Note: The extra space is only for the array to be returned.
Try and perform all operations within the provided array. 

Example 1:

Input:
N = 4
a[] = {0,3,1,2}
Output: -1
Explanation: There is no repeating element in the array.Therefore output is -1.
Example 2:

Input:
N = 5
a[] = {2,3,1,2,3}
Output: 2 3 
Explanation: 2 and 3 occur more than once
in the given array.
Your Task:
Complete the function duplicates() which takes array a[] and n as input as parameters and returns a list of elements that occur more than once in the given array in a sorted manner. If no such element is found, return list containing [-1]. 
