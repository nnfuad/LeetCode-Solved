class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Convert string to integer following atoi rules.
        
        Args:
            s: Input string to convert
        
        Returns:
            32-bit signed integer representation of the string
        """
        # Define 32-bit signed integer bounds
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        # Step 1: Skip leading whitespace
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1
        
        # If we've reached the end, no valid number
        if i == n:
            return 0
        
        # Step 2: Determine the sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        # Step 3: Read in the integer
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            num = num * 10 + digit
            i += 1
        
        # Apply the sign
        num *= sign
        
        # Step 4: Clamp to 32-bit range
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        
        return num