def merge(arr):

    arr.sort()

    ans= [arr[0]]

    for i in range(1,len(arr)):

        curr_start = arr[i][0]

        curr_end = arr[i][1]

        last_arr = ans[-1]
        last_start = last_arr[0]
        last_end = last_arr[-1]

        if curr_start <= last_end:
            #overlap
            if curr_end >last_end:
                last_arr[1] =curr_end

        else:
            ans.append([curr_start, curr_end])

    return ans

arr = [[1,3],[2,6],[8,10],[15,18]]
print(merge(arr))