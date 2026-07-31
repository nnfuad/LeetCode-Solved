class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        
        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with absolute values
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)
        
        quotient = 0
        
        while dividend_abs >= divisor_abs:
            temp = divisor_abs
            shift = 0
            # Find the maximum shift such that temp << shift <= dividend_abs
            while (temp << 1) <= dividend_abs:
                temp <<= 1
                shift += 1
            # Add the corresponding power of two to the quotient
            quotient += (1 << shift)
            # Subtract the found value from the dividend
            dividend_abs -= temp
        
        # Apply the sign
        if negative:
            quotient = -quotient
        
        # Clamp to 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if quotient > INT_MAX:
            return INT_MAX
        elif quotient < INT_MIN:
            return INT_MIN
        else:
            return quotient