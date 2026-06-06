def avgsub(nums,k):
    window_sum = sum(nums[:k])
    max_sum = window_sum 

    for i in range(k,len(nums)):
        # add element
        window_sum += nums[i]

        #remove element
        window_sum -= nums[i-k]

        max_sum = max(max_sum,window_sum)

    return max_sum/k

nums = [1,12,-5,-6,50,3]
k=4
print(avgsub(nums,k))