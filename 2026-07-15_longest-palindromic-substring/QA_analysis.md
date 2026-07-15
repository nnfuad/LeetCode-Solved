# Longest Palindromic Substring

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/longest-palindromic-substring/

---

### Problem Analysis
The problem requires finding the longest contiguous substring in a given string that is a palindrome. A palindrome reads the same forwards and backwards. The constraints (string length up to 1000) suggest that an O(n^2) solution is acceptable.

### Optimal Approach
The **Expand Around Center** method is chosen for its efficiency and simplicity. This approach works by treating each character (and the space between characters) as potential centers of a palindrome and expanding outward as long as the characters on both ends match.

#### Key Insights:
1. **Odd and Even Length Palindromes**: A palindrome can be centered at a single character (odd length) or between two characters (even length).
2. **Expansion**: For each center, expand as far left and right as possible while the characters match.
3. **Tracking the Longest**: Keep track of the maximum length palindrome found during the expansion process.

#### Time and Space Complexity:
- **Time Complexity**: O(n^2), where n is the length of the string. Each of the n centers can expand up to O(n) times.
- **Space Complexity**: O(1), as we only use a few variables to track the longest palindrome.

### Solution Code
The code implements the expand around center approach by iterating through each character, expanding for both odd and even length palindromes, and updating the longest found substring accordingly.