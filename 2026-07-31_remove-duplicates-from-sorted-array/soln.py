class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Handle edge case (though constraints say length >= 1)
        if not nums:
            return 0
        
        # Initialize write pointer at 1 (first element is always unique)
        k = 1
        
        # Iterate through array starting from second element
        for i in range(1, len(nums)):
            # If current element differs from previous, it's a new unique value
            if nums[i] != nums[i - 1]:
                # Place it at the next available position
                nums[k] = nums[i]
                # Move write pointer forward
                k += 1
        
        # Return count of unique elements
        return k