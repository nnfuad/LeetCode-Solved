class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculate the number of distinct ways to climb n stairs.
        You can climb either 1 or 2 steps at a time.
        
        Args:
            n: Number of steps in the staircase (1 <= n <= 45)
        
        Returns:
            Number of distinct ways to reach the top
        """
        # Handle base cases
        if n <= 2:
            return n
        
        # Initialize previous two values
        # prev2 represents ways(n-2), prev1 represents ways(n-1)
        prev2, prev1 = 1, 2
        
        # Build up the solution iteratively
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2, prev1 = prev1, current
        
        return prev1