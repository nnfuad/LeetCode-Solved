class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        min_diff = abs(closest_sum - target)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, n-1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                diff = abs(current_sum - target)
                if diff == 0:
                    return current_sum
                if diff < min_diff:
                    min_diff = diff
                    closest_sum = current_sum
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        return closest_sum