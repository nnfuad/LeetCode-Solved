class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start = 0
        end = 0
        
        def expand(l: int, r: int) -> tuple:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return (l + 1, r - 1)
        
        for i in range(len(s)):
            # Odd length palindromes
            l1, r1 = expand(i, i)
            # Even length palindromes
            l2, r2 = expand(i, i + 1)
            
            # Update longest palindrome found
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        
        return s[start:end + 1]