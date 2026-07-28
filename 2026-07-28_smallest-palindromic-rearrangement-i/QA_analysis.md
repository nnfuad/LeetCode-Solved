# Smallest Palindromic Rearrangement I

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

---

# Smallest Palindromic Rearrangement I

## Problem Understanding
We are given a palindromic string `s` and need to find the lexicographically smallest palindromic permutation of `s`.

### Key Observations:
1. A palindrome reads the same forwards and backwards
2. For a palindrome of length n, the first half determines the second half
3. At most one character can have an odd count (the middle character for odd-length strings)
4. Since input is guaranteed palindromic, the odd-count condition is satisfied

## Optimal Approach
To get the lexicographically smallest palindrome:
1. Count character frequencies
2. Build the first half by taking half of each character count (sorted lexicographically)
3. If length is odd, the middle character is the one with odd count
4. The second half is the reverse of the first half

### Time Complexity: O(n log n) where n is the length of s
- Counting characters: O(n)
- Building first half string: O(n)
- Sorting the first half: O(k log k) where k is the number of unique characters in first half, but k ≤ n/2
- Overall: O(n)

### Space Complexity: O(n) for storing the result and intermediate strings

## Solution Strategy
1. Count frequency of each character
2. Build first half: for each character in sorted order, add (count/2) copies
3. Find middle character if string length is odd
4. Construct result: first_half + middle + reverse(first_half)

## Implementation Details
- Use collections.Counter or defaultdict for character counting
- Sort characters to ensure lexicographically smallest arrangement
- Handle edge case of single character string

## Edge Cases
- Single character string (already smallest)
- All characters same
- Even length strings (no middle character)
- Odd length strings (one middle character with odd count)