class Solution:
    def longestCommonSubsequence(self, text1, text2):
        dp ={}
        def solve(i,j):

            #base
            if i==0 or j==0:
                return 0
            if (i,j) in dp:
                return dp[(i, j)]
            #match hua toh dono -1
            if text1[i-1] == text2[j-1]:
                dp[(i,j)] =  1 + solve(i-1,j-1)
            
            else:    #no match so ones i-1 and j-1
                dp[(i,j)] = max(solve(i,j-1),solve(i-1,j))
            
            return dp[(i, j)]

        return solve(len(text1),len(text2))
