# Find the Index of the First Occurrence in a String

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

---

The problem requires finding the first occurrence of a substring (needle) within a string (haystack). The straightforward approach is to iterate over each possible starting position in the haystack and check if the substring from that position matches the needle. This approach has a time complexity of O(N*M), where N is the length of the haystack and M is the length of the needle. While this might seem inefficient for large inputs, the constraints (up to 10^4 for both lengths) make this approach feasible. The solution handles edge cases such as when the needle is longer than the haystack or when the needle is found at the very end of the haystack. The code is simple and leverages Python's string slicing for easy comparison.

**Optimal Approach:**
The naive approach is sufficient here. For each starting index in the haystack (up to `len(haystack) - len(needle)`), compare the substring of length `len(needle)` with the needle. Return the first index where a match is found, or -1 if no match exists.

**Time and Space Complexity:**
- **Time Complexity:** O(N*M), where N is the length of the haystack and M is the length of the needle. In the worst case, each character comparison takes O(M) time, and there are O(N) starting positions to check.
- **Space Complexity:** O(1), as no additional space is used beyond the input variables.

The solution is implemented using Python's string slicing and comparison, which is efficient for the given problem constraints.