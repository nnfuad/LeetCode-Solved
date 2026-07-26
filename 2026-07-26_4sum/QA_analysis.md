# 4Sum

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/4sum/

---

The problem requires finding all unique quadruplets in an array that sum to a given target. The optimal approach uses sorting and two pointers to achieve O(n^3) time complexity, which is feasible for n up to 200. Sorting the array allows efficient duplicate handling and two-pointer traversal. The steps are:

1. Sort the array to facilitate duplicate skipping and two-pointer search.
2. Iterate over the first two elements (i and j) with nested loops, skipping duplicates using their indices.
3. For each pair (i, j), use two pointers (left and right) to find the remaining two elements.
4. Adjust pointers based on whether the current sum is less than, greater than, or equal to the target.
5. When a valid quadruplet is found, add it to the result and skip duplicates by moving pointers past all identical values.

Time Complexity: O(n^3) due to three nested loops (i, j, and the two-pointer traversal).
Space Complexity: O(1) (excluding the output list).