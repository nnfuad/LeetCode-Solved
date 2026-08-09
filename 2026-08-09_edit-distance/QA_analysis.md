# Edit Distance

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/edit-distance/

---

The Edit Distance problem is a classic dynamic programming problem where we need to find the minimum number of operations (insert, delete, replace) required to convert one string into another. The optimal approach uses a 2D DP table where `dp[i][j]` represents the minimum edit distance between the first `i` characters of `word1` and the first `j` characters of `word2`. The base cases are when one string is empty, requiring all characters of the other to be inserted or deleted. For transitions, if characters match, the distance remains the same as the previous state. Otherwise, we take the minimum of three possible operations (replace, delete, insert) and add 1. This solution has a time and space complexity of O(m*n), where m and n are the lengths of the input strings. Given the problem constraints (max 500 characters), this approach is efficient and straightforward.