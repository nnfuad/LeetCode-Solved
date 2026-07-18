class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x: int) -> bool:
            """Check if x is prime using 6k±1 optimization."""
            if x < 2:
                return False
            if x == 2 or x == 3:
                return True
            if x % 2 == 0 or x % 3 == 0:
                return False
            i = 5
            while i * i <= x:
                if x % i == 0 or x % (i + 2) == 0:
                    return False
                i += 6
            return True
        
        def generate_odd_palindromes(start: int):
            """Generate odd-length palindromes >= start in increasing order."""
            length = len(str(start))
            
            # Start with the next odd length if current length is even
            if length % 2 == 0:
                length += 1
            
            while True:
                half = (length + 1) // 2
                min_prefix = 10 ** (half - 1)
                max_prefix = 10 ** half - 1
                
                for prefix in range(min_prefix, max_prefix + 1):
                    prefix_str = str(prefix)
                    # Create palindrome: prefix + reverse of prefix without last char
                    palindrome = int(prefix_str + prefix_str[:-1][::-1])
                    if palindrome >= start:
                        yield palindrome
                
                length += 2
        
        # Handle small values of n
        if n <= 11:
            for p in [2, 3, 5, 7, 11]:
                if p >= n:
                    return p
        
        # Find the smallest prime palindrome >= n
        for palindrome in generate_odd_palindromes(n):
            if is_prime(palindrome):
                return palindrome
        
        # The problem guarantees an answer exists, so we should never reach here
        return -1