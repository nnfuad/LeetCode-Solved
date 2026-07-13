class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        last_occurrence = {}
        
        for right in range(len(s)):
            char = s[right]
            if char in last_occurrence and last_occurrence[char] >= left:
                left = last_occurrence[char] + 1
            last_occurrence[char] = right
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length
        
        return max_length