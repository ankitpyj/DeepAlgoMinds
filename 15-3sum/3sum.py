class Solution(object):
    def threeSum(self, nums):
        
        

        ans = set()

        for i in range(len(nums)):
            hashmap = {}
        
            for j in range(i+1,len(nums)):
                exist = nums[i] + nums[j]
                k= -exist

                if k in hashmap:
                    ans.add(tuple(sorted([nums[i], nums[j], k])))
                    # ans.add(nums[i],nums[j],k)

                hashmap[nums[j]] = j
        listt=[]    
        for x in ans:
            listt.append(x)

        return listt




        