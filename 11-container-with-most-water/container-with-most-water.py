class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) -1

        max_area = 0

        while left < right:
            width = right - left 
            # height1 = min(height[left],height[right])
            
            # curr_area = width * height1
            curr_area = (right - left) * min(height[left], height[right])

            max_area = max(curr_area,max_area)

            if height[left] < height[right]:
                left +=1
            else:
                right -=1

        return max_area