def maxproduct(nums):

    nums.sort()

    a = nums[-1] * nums[-2] * nums[-3]  # lat 3 nuber

    b = nums[0] * nums[1] * nums[-1]  # starting 2 * last 1

    return max(a,b)

nums=[1,2,3]
nums = [-10, -10, 1, 2, 3]
print(maxproduct(nums))


# def maximumProduct(nums):

#     max1 = max2 = max3 = float('-inf')
#     min1 = min2 = float('inf')

#     for num in nums:

#         # largest 3
#         if num > max1:
#             max3 = max2
#             max2 = max1
#             max1 = num

#         elif num > max2:
#             max3 = max2
#             max2 = num

#         elif num > max3:
#             max3 = num

#         # smallest 2
#         if num < min1:
#             min2 = min1
#             min1 = num

#         elif num < min2:
#             min2 = num

#     return max(
#         max1 * max2 * max3,
#         min1 * min2 * max1
#     )