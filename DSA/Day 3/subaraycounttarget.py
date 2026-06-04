def subarraySum(nums, k):
    count = 0

    for i in range(0,len(nums)):
        curr_sum = 0

        for j in range(i,len(nums)):
            curr_sum += nums[j]

            if curr_sum == k:
                count +=1
    return count

nums=[1,1,1]
k =2
print(subarraySum(nums,k))
