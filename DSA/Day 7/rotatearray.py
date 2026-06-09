# def findMin(nums):

#     left = 0
#     right = len(nums) - 1

#     while left < right:

#         mid = (left + right) // 2

#         if nums[mid] > nums[right]:
#                 # Minimum is in the right half
#             left = mid + 1
#         else:
#                 # Minimum is at mid or in the left half
#             right = mid

#     return nums[left]

# nums = [3,4,5,1,2]
# print(findMin(nums))


def findMin(nums):

    left = 0
    right = len(nums) - 1

    while left < right:

        mid = (left + right) // 2
        
        if nums[mid] < nums[0]:
            if nums[-1]<nums[mid]:
                left=mid+1
            else:
                return nums[-1]            
            
        else:
            end=mid-1
        
    return 
        
        
        
