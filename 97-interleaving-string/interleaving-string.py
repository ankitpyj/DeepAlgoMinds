class Solution(object):
    def isInterleave(self, s1, s2, s3):

        if (len(s1) + len(s2) != len(s3)):
            return False

        memo ={}
        def solve(i,j):
            k=i+j

            result = False

            if (i == len(s1) and j == len(s2)):
                return True

            if (i, j) in memo:
                return memo[(i, j)]

            if i < len(s1) and s1[i]==s3[k]:
                result =  solve(i+1,j)

            if result == True:
                return result
            
            if j < len(s2) and s2[j]==s3[k]:
                result = solve(i,j+1)

            memo[(i, j)] = result

            return result

        return solve(0,0)