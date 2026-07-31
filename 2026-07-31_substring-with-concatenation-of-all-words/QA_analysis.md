# Substring with Concatenation of All Words

**Difficulty:** Hard

**Link:** https://leetcode.com/problems/substring-with-concatenation-of-all-words/

---

## Problem Analysis

### Understanding the Problem
We need to find all starting indices in string `s` where a concatenated substring exists. A concatenated substring is formed by concatenating all strings from the `words` array in any permutation.

### Key Observations
1. All words have the same length (let's call it `word_length`)
2. The concatenated string has a fixed total length: `words.length * word_length`
3. We need to find substrings that are exactly the concatenation of all words
4. Words can have duplicates (e.g., ["word", "word"])

### Approach Selection
**Brute Force:**
- Generate all permutations of words
- For each permutation, check if it exists in s
- Time: O(n! * n) where n is the number of words - Too slow

**Optimized Sliding Window Approach:**
Since all words have the same length, we can use a clever sliding window technique:

1. For each possible starting offset (0 to word_length-1):
   - Use a sliding window moving in steps of word_length
   - Maintain a frequency map of words in the current window
   - Adjust window size when we encounter words not in the target list or exceed counts

### Algorithm Explanation
```python
# For each offset from 0 to word_length-1:   
#   Initialize left pointer, right pointer, window counter   
#   While right + word_length <= len(s):   
#     Extract word at position right   
#     If word is in target:   
#       Increment its count in window   
#       Shrink window if count exceeds target   
#       If window size matches total length, add left to result   
#     Else:   
#       Reset window and move left to right   
#     Move right by word_length
```

### Time and Space Complexity
- **Time Complexity:** O(L * word_length) where L is the length of string s
  - We iterate through s word_length times (once for each offset)
  - Each iteration is O(L / word_length) = O(L)
  - Overall: O(L * word_length)
  - Since word_length ≤ 30, effectively O(L)

- **Space Complexity:** O(U) where U is the number of unique words
  - We store frequency maps for target words and current window
  - In worst case, U ≤ words.length ≤ 5000

### Edge Cases Handled
1. Single word in words array
2. Duplicate words in words array
3. No valid concatenated substrings
4. Overlapping valid substrings