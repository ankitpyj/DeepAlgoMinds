def singlenum(nums):
    ans = set()
    for i in nums:
        if i in ans:
            ans.remove(i)
        else:
            ans.add(i)

    # return int(list(ans)[0])
    return ans.pop()
nums = [2,2,1]
print(singlenum(nums))


# def singleNumber(nums):

#     ans = 0

#     for num in nums:
#         ans ^= num

#     return ans