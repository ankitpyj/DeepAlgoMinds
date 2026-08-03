class Solution(object):
    def setZeroes(self, matrix):

        row = len(matrix)
        col = len(matrix[0])

        row_visit = [False] * row
        col_visit = [False] * col

        for i in range(row):
            for j in range(col):
                
                if matrix[i][j] == 0:

                    row_visit[i] =True
                    col_visit[j] = True

        for i in range(row):
            for j in range(col):
                if row_visit[i] or col_visit[j]:
                    matrix[i][j] = 0
        