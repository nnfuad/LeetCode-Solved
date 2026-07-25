# Longest Common Prefix

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/longest-common-prefix/

---

The problem requires finding the longest common prefix among an array of strings. The optimal approach involves iterating through each character of the first string and checking if all other strings have the same character at the corresponding position. The steps are as follows:

1. **Edge Cases Handling**: If the input array is empty, return an empty string (though constraints ensure it's non-empty).
2. **Reference String**: Use the first string as the reference for comparison.
3. **Character-by-Character Check**: For each character index in the reference string:
   - Compare the character with the same index in all other strings.
   - If any string is shorter than the current index or has a different character, return the prefix up to the previous index.
4. **Complete Match**: If all characters of the reference string are matched, return the entire reference string.

**Time Complexity**: O(m * n), where m is the length of the first string and n is the number of strings. In the worst case, all characters of the first string are checked against all other strings.

**Space Complexity**: O(1), as no additional data structures are used beyond a few variables.

This approach is efficient and straightforward, ensuring minimal overhead while correctly handling all edge cases.