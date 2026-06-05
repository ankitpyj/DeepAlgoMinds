def thirdMax(nums):
    nums = list(set(nums))
    nums.sort()

    if len(nums) >= 3:
        return nums[-3]

    return nums[-1]
    
nums = [1,2,2,3,4,5,67,81]
print(thirdMax(nums))



# class Solution:
#     def thirdMax(self, nums):

#         first = second = third = float('-inf')

#         for num in nums:

#             if num in (first, second, third):
#                 continue

#             if num > first:
#                 third = second
#                 second = first
#                 first = num

#             elif num > second:
#                 third = second
#                 second = num

#             elif num > third:
#                 third = num

#         if third == float('-inf'):
#             return first

#         return third