class Solution(object):
    def hammingWeight(self, n):
        count = 0
        
        while n>0:
            rem=n%2  # remainder(last digit) 
            if rem ==1:
                count+=1
            n =n//2
        return count 
