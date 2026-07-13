# Longest Substring Without Repeating Characters

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/longest-substring-without-repeating-characters/

---

The problem requires finding the length of the longest substring without repeating characters in a given string. The optimal approach uses a sliding window technique combined with a hash map to track the last occurrence of each character. This allows efficient tracking of the current valid window and adjusting the window's left boundary when a duplicate is encountered. The time complexity is O(n) as each character is processed exactly once, and the space complexity is O(min(n, m)) where m is the size of the character set (typically O(1) for fixed character sets).