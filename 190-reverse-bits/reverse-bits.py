class Solution(object):
    def reverseBits(self, n):

        binary =""
        while n>0:
            rem = n%2
            binary= str(rem) + binary
            n=n//2
        binary = binary.zfill(32)
        reversed_binary = binary[::-1]

        return int(reversed_binary,2)

        
        