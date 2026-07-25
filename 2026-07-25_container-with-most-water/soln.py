class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            width = right - left
            if height[left] < height[right]:
                area = height[left] * width
                left += 1
            else:
                area = height[right] * width
                right -= 1
            max_area = max(max_area, area)
        return max_area