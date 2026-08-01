# Search Insert Position

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/search-insert-position/

---

### Problem Analysis:
The problem requires finding the index of a target in a sorted array of distinct integers, or returning the insertion position if the target is not found. The key constraint is achieving O(log n) runtime, which mandates the use of binary search.

### Approach:
Binary search is ideal here because the array is sorted. The algorithm narrows down the search space by half in each iteration:
1. Initialize `left` and `right` pointers.
2. While `left <= right`, compute the middle index.
3. If the middle element equals the target, return its index.
4. Adjust `left` or `right` based on whether the target is less than or greater than the middle element.
5. When the loop exits, `left` points to the insertion position (the index where the target would fit in the sorted order).

### Time Complexity:
- **O(log n)**: Binary search halves the search space each iteration.

### Space Complexity:
- **O(1)**: Uses constant extra space for pointers.

### Edge Cases Covered:
- Target smaller than all elements (returns 0).
- Target larger than all elements (returns array length).
- Target exists at the start, middle, or end (returns exact index).

### Solution Code:
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
```

This implementation efficiently handles all cases by leveraging binary search to meet the required time complexity.