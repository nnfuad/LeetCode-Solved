# First Missing Positive

**Difficulty:** Hard

**Link:** https://leetcode.com/problems/first-missing-positive/

---

# First Missing Positive - Problem Analysis

## Problem Understanding
We need to find the smallest positive integer that is not present in the array. The key constraints are O(n) time complexity and O(1) auxiliary space.

## Key Insights
1. **Answer Range**: The answer is always in the range [1, n+1] where n is the array length. This is because:
   - If all numbers 1 to n are present, the answer is n+1
   - If any number from 1 to n is missing, the answer is at most n

2. **In-place Hashing**: We can use the array itself as a hash table by placing each positive number x (where 1 ≤ x ≤ n) at index x-1

## Optimal Approach: Cyclic Sort
The algorithm uses cyclic sort principles:

1. **Place Elements**: Iterate through the array, placing each valid positive integer x (1 ≤ x ≤ n) at position x-1 via swapping
2. **Find Missing**: After rearrangement, scan the array. The first index i where nums[i] ≠ i+1 gives us the answer (i+1)
3. **Edge Case**: If all positions are correct, return n+1

## Time Complexity: O(n)
- Each element is swapped at most once to its correct position
- The swapping loop runs in amortized constant time per element

## Space Complexity: O(1)
- We only use the input array for rearrangement, no additional data structures

## Example Walkthroughs

**Example 1**: nums = [1,2,0]
- Rearrange: [1,2,0] (already in correct positions for 1,2)
- At index 2: nums[2] = 0 ≠ 3, so answer is 3

**Example 2**: nums = [3,4,-1,1]
- After rearrangement: [1,-1,3,4]
- At index 1: nums[1] = -1 ≠ 2, so answer is 2

**Example 3**: nums = [7,8,9,11,12]
- All numbers > n, no valid numbers to place
- At index 0: nums[0] = 7 ≠ 1, so answer is 1