class Solution:
    def missingNumber(self,array,n):
       array.sort()
       array.append(0)
       for i in range(0,n):
           if array[i]!=i+1:
               for j in range(0,n):
                   if array[j]==0:
                       array[j]+=i+1
                       return array[j]
        
