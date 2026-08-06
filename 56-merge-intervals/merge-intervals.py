class Solution(object):
    def merge(self, intervals):
        intervals.sort()

        ans =[intervals[0]]
        
        for i in range(1,len(intervals)):
            
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]

            last_arr = ans[-1]

            last_start = last_arr[0]
            last_end = last_arr[-1]

            # overlap

            if curr_start <= last_end:
                last_arr[1] = max(curr_end ,last_end)

            else:
                ans.append([curr_start,curr_end])

        return ans




        