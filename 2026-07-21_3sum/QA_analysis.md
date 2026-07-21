# 3Sum

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/3sum/

---

# 3Sum Problem Analysis

## Problem Understanding
Given an integer array `nums`, find all unique triplets `[nums[i], nums[j], nums[k]]` where:
- All three indices are distinct (`i != j`, `i != k`, `j != k`)
- The sum equals zero: `nums[i] + nums[j] + nums[k] == 0`
- No duplicate triplets in the result

## Optimal Approach: Sorting + Two Pointers

### Algorithm Steps:
1. **Sort the array** - Enables efficient duplicate handling and two-pointer traversal
2. **Iterate with a fixed element** - For each element at index `i`, treat it as the first element of potential triplets
3. **Two-pointer search** - Use left and right pointers on the remaining subarray to find pairs that sum to `-nums[i]`
4. **Skip duplicates** - Avoid duplicate triplets by skipping equal values during iteration

### Key Insight:
After sorting, if `nums[i] + nums[left] + nums[right] == 0`:
- If we found a valid triplet, move both pointers and skip any duplicates
- If sum < 0, we need a larger sum, so move left pointer right
- If sum > 0, we need a smaller sum, so move right pointer left

### Time Complexity: O(n²)
- Sorting: O(n log n)
- Outer loop: O(n)
- Inner two-pointer loop: O(n) per iteration
- Total: O(n log n) + O(n²) = O(n²)

### Space Complexity: O(1)
- In-place sorting (not counting output array)
- Only a few variables for pointers and iteration

## Edge Cases Handled:
1. All zeros: `[0,0,0]` → `[[0,0,0]]`
2. No valid triplets: `[0,1,1]` → `[]`
3. Multiple duplicates: `[-2,-2,0,0,2,2]` → `[[-2,0,2]]`
4. Negative numbers: Standard two-pointer handles all ranges

## Duplicate Avoidance Strategy:
- Skip duplicate first elements: `if i > 0 and nums[i] == nums[i-1]: continue`
- After finding triplet, skip duplicates for second and third elements using adjacent comparisons

This approach is optimal because it eliminates the brute-force O(n³) solution and the hash-based O(n²) approach by leveraging the sorted property for efficient duplicate detection.