# Remove Duplicates from Sorted Array

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/remove-duplicates-from-sorted-array/

---

## Problem Analysis

Given a sorted array in non-decreasing order, we need to remove duplicates in-place such that each unique element appears only once. The key requirements are:
1. Return the count of unique elements (k)
2. Maintain relative order of elements
3. Modify the array in-place (O(1) space)
4. The first k elements should contain unique values in sorted order

## Optimal Approach

The optimal solution uses a **two-pointer technique**:

### Algorithm:
1. Initialize a write pointer `k` starting at 1 (since the first element is always unique)
2. Iterate through the array with a read pointer `i` starting from index 1
3. If the current element differs from the previous element, it's a new unique value:
   - Place it at position `k`
   - Increment `k`
4. Return `k` as the count of unique elements

### Time Complexity: O(n)
We make a single pass through the array.

### Space Complexity: O(1)
We modify the array in-place without using additional storage.

## Why This Works
Since the array is sorted, duplicates are adjacent. By comparing each element with its predecessor, we can identify unique values. The write pointer `k` always points to the next available position for a unique element, ensuring the first `k` elements are the deduplicated result.

## Edge Cases Handled
- Single element: Returns 1
- All duplicates: Returns 1
- All unique: Returns array length
- Mixed duplicates: Correctly counts and places unique elements