class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # saare 0 ke (row,col) meh queue meh daaldunga or baaki ko -1 then 
        # fixed direction top(-1,0) ,bottom(1,0) ,left(0,-1), right(0,1)

        # ab queue meh seh row ,col ko pop krta jaunga and
        #  matrix bnata jaunga but check krunga boundary cond and jha -1 hoga usko meh old matrix +1 krta jaunga


        m = len(mat)
        n =len(mat[0])

        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] = -1

        #  directions
        directions = [
            (-1, 0),   # up
            (1, 0),    # down
            (0, -1),   # left
            (0, 1)     # right
        ]
        
        while queue:

            row,col = queue.popleft()


            for dr,dc in directions:

                new_row =  row + dr
                new_col = col +dc


                # check

                if (0<=new_row<m) and (0<=new_col<n ) and (mat[new_row][new_col]== -1):
                    mat[new_row][new_col] = mat[row][col] +1

                    queue.append((new_row, new_col))
        return mat