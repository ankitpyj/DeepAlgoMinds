def findDuplicate(nums):
    modify =[]
    # for i in nums:      #O(n)
    #     if i in modify:  #O(n)
    #         return i 
    #     modify.append(i)


    seen =set()  
    for i in nums:  #O(n)
        if i in seen:   #O(1)
            return i 
        seen.add(i)

nums = [1,3,4,2,3]
print(findDuplicate(nums))



