class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        prev_dp = [False] * (m + 1)
        prev_dp[0] = True  # Base case: empty pattern matches empty string
        
        # Initialize first row (i=0, empty string s)
        for j in range(1, m + 1):
            if p[j - 1] == '*':
                prev_dp[j] = prev_dp[j - 1]
            else:
                prev_dp[j] = False
        
        # Process each character in s
        for i in range(1, n + 1):
            curr_dp = [False] * (m + 1)
            curr_dp[0] = False  # Non-empty s cannot match empty pattern
            for j in range(1, m + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    curr_dp[j] = prev_dp[j - 1]
                elif p[j - 1] == '*':
                    curr_dp[j] = curr_dp[j - 1] or prev_dp[j]
                else:
                    curr_dp[j] = False
            prev_dp = curr_dp  # Update previous row for next iteration
        
        return prev_dp[m]