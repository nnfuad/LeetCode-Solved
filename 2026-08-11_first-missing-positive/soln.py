class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Place each positive integer x (1 <= x <= n) at position x-1
        for i in range(n):
            # Keep swapping until current position has correct number or invalid number
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with nums[nums[i] - 1]
                correct_pos = nums[i] - 1
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        
        # Find the first position where nums[i] != i+1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # All positions filled correctly, answer is n+1
        return n + 1