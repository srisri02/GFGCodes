#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        #Your code here
        x = max(arr)
        if(x<=0):
            return 1
        for i in range(1,x+1):
            if i not in arr:
                return i
        return i+1
      

Problem : You are given an array arr[] of N integers. The task is to find the smallest positive number missing from the array.

Note: Positive number starts from 1.

Example 1:

Input:
N = 5
arr[] = {1,2,3,4,5}
Output: 6
Explanation: Smallest positive missing 
number is 6.
Example 2:

Input:
N = 5
arr[] = {0,-10,1,3,-20}
Output: 2
Explanation: Smallest positive missing 
number is 2.
Your Task:
The task is to complete the function missingNumber() which returns the smallest positive missing number in the array.
