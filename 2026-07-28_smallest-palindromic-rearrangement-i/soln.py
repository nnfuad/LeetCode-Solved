class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        
        # Count character frequencies
        from collections import Counter
        count = Counter(s)
        
        # Build the first half of the palindrome
        first_half = []
        for char in sorted(count.keys()):
            first_half.append(char * (count[char] // 2))
        
        first_half = ''.join(first_half)
        
        # Find middle character if exists
        middle = ''
        if n % 2 == 1:
            for char in count:
                if count[char] % 2 == 1:
                    middle = char
                    break
        
        # Construct the full palindrome
        return first_half + middle + first_half[::-1]