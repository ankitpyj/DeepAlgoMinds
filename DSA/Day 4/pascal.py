def pascal(numRows):

    ans = [[1]]

    for i in range(1,numRows):
        
        prev = ans[-1]
        
        #first =1 , middle = len(prev)-1 ,last =1
        
        # first
        row= [1]

        #middle
        for j in range(1,len(prev)):
            row.append(prev[j-1] + prev[j] )

        #last 
        row.append(1)

        ans.append(row)

    return ans


numRows = 5
print(pascal(numRows))