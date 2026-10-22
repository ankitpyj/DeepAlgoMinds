class Solution(object):
    def hammingWeight(self, n):
        count =0
        while n>0:
            x= n&1  # check last set bits 
            count+=x
            n = n>>1 #rightshift 

        return count
