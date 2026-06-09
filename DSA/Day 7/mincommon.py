# def getcommmon(nums1,nums2):
    
    
    
#     for i in range(len(nums1)):
#         for j in range(len(nums2)):
            
#             if nums1[i]== nums2[j]:
#                 return nums1[i]
        
#     return -1
    
# nums1 = [1,2,3]
# nums2 = [2,4]
# print(getcommmon(nums1, nums2))

def getcommon(nums1,nums2):
     
    i=j=0
    
    while i<len(nums1) and j<len(nums2):
        
        if nums1[i] ==nums2[j]:
            return nums1[i]
        
        elif nums1[i] < nums2[j]:
            i=i+1
        
        else:
            j =j+1
    
    return -1 

nums1 = [1,2,3]
nums2 = [2,4]
print(getcommon(nums1, nums2))