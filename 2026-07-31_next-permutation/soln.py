class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        Finds the next lexicographically greater permutation of nums in-place.
        If no such permutation exists, rearranges nums to the smallest order.
        """
        n = len(nums)
        
        # Step 1: Find the first index from the right where nums[i] < nums[i+1]
        # This is the pivot point where we can make a larger permutation
        pivot = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break
        
        # If no pivot found, the array is in descending order (largest permutation)
        # Reverse entire array to get the smallest permutation
        if pivot == -1:
            self._reverse(nums, 0, n - 1)
            return
        
        # Step 2: Find the smallest element to the right of pivot that is greater than nums[pivot]
        # Since the suffix is in descending order, we scan from right to left
        swap_idx = -1
        for j in range(n - 1, pivot, -1):
            if nums[j] > nums[pivot]:
                swap_idx = j
                break
        
        # Step 3: Swap the pivot with the swap candidate
        nums[pivot], nums[swap_idx] = nums[swap_idx], nums[pivot]
        
        # Step 4: Reverse the suffix to get the smallest order for that suffix
        self._reverse(nums, pivot + 1, n - 1)
    
    def _reverse(self, nums: List[int], left: int, right: int) -> None:
        """Helper method to reverse a portion of the array in-place."""
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1