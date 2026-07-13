class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        # Ensure nums1 is the smaller array for efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2
        
        left, right = 0, m
        
        while left <= right:
            partition_x = (left + right) // 2
            partition_y = total_left - partition_x
            
            # Handle edge cases with boundary values
            max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
            min_right_x = float('inf') if partition_x == m else nums1[partition_x]
            
            max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
            min_right_y = float('inf') if partition_y == n else nums2[partition_y]
            
            # Check if we found the correct partition
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                # Correct partition found
                if (m + n) % 2 == 0:
                    # Even total length - average of two middle elements
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2.0
                else:
                    # Odd total length - single middle element
                    return float(max(max_left_x, max_left_y))
            elif max_left_x > min_right_y:
                # Too many elements from nums1 on left side
                right = partition_x - 1
            else:
                # Too few elements from nums1 on left side
                left = partition_x + 1
        
        return 0.0  # Should not reach here with valid input