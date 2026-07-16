class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        num = abs(x)
        reversed_num = 0
        max_abs = 2**31  # 2147483648
        while num > 0:
            digit = num % 10
            if reversed_num > max_abs // 10 or (reversed_num == max_abs // 10 and digit > max_abs % 10):
                return 0
            reversed_num = reversed_num * 10 + digit
            num = num // 10
        reversed_num *= sign
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        return reversed_num