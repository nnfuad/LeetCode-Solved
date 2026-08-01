# Find First and Last Position of Element in Sorted Array

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

---

The problem requires finding the first and last occurrences of a target value in a sorted array with O(log n) time complexity. Using linear search is not feasible due to the constraint. The optimal approach uses binary search twice: once to find the first occurrence (lower bound) and once to find the upper bound. The first occurrence is found by adjusting the binary search to move right when the middle element is less than the target, otherwise moving left. The upper bound is found by moving left when the middle element is less than or equal to the target. The upper bound gives the insertion point after the last target occurrence; hence, the last occurrence is at upper_bound -1. This approach ensures logarithmic time complexity and constant space usage.

The steps are:
1. Handle edge case of empty array.
2. Find the first occurrence using a lower bound binary search.
3. If the first occurrence is not found, return [-1, -1].
4. Find the upper bound to determine the ending index.
5. Return the first and last indices computed.