def adddigit(nums):
    
    
    while nums >=10 :
        total = 0

        while nums>0:
            digit = nums % 10
            total += digit
            nums =nums//10
    
        nums = total
    
    return nums
    

n = 199
print(adddigit(n))




# class Solution(object):
#     def addDigits(self, num):
#         total = 0
        
#         while num>0:
#             digit = num % 10
#             total += digit
#             num =num//10
    
#         new_total =0
#         while total>0:
#             digit_total = total % 10
#             new_total += digit_total
#             total = total // 10
#         return new_total