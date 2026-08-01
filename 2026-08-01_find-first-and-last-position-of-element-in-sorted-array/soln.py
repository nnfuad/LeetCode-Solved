class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        
        # Find first occurrence (lower bound)
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        first = left if left < len(nums) and nums[left] == target else -1
        
        if first == -1:
            return [-1, -1]
        
        # Find upper bound
        left_upper = 0
        right_upper = len(nums)
        while left_upper < right_upper:
            mid = (left_upper + right_upper) // 2
            if nums[mid] <= target:
                left_upper = mid + 1
            else:
                right_upper = mid
        
        last = left_upper - 1
        return [first, last]