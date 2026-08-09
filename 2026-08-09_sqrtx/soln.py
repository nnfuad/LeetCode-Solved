class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Compute the integer square root of x using binary search.
        
        Args:
            x: A non-negative integer
        
        Returns:
            The square root of x rounded down to the nearest integer
        """
        # Handle edge cases where x is 0 or 1
        if x < 2:
            return x
        
        # Initialize binary search bounds
        left, right = 1, x // 2
        
        # Binary search for the integer square root
        while left <= right:
            # Calculate mid-point to avoid potential overflow
            mid = (left + right) // 2
            
            # Check if mid squared is less than or equal to x
            if mid * mid <= x:
                # mid could be the answer, but we look for the maximum valid one
                left = mid + 1
            else:
                # mid squared is too large, search in lower half
                right = mid - 1
        
        # After the loop, right is the largest integer where right^2 <= x
        return right