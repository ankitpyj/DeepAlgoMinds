def searchRange(nums, target):

    # first position
    left, right = 0, len(nums) - 1
    first_pos = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            first_pos = mid
            right = mid - 1

        elif nums[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    # last position
    left, right = 0, len(nums) - 1
    last_pos = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            last_pos = mid
            left = mid + 1

        elif nums[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return [first_pos, last_pos]


nums = [5,7,7,8,8,10]
target = 8

print(searchRange(nums, target))