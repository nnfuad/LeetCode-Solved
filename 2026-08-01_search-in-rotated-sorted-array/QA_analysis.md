# Search in Rotated Sorted Array

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/search-in-rotated-sorted-array/

---

## Problem Analysis

### Problem Understanding
This is a classic binary search variant problem. We have a sorted array that has been left-rotated at an unknown pivot point. The task is to search for a target value with O(log n) time complexity.

### Key Insights
1. **At least half is always sorted**: In any rotated sorted array, at least one half (left or right of mid) will always be in sorted order.
2. **Binary search modification**: We can modify standard binary search to handle the rotation by identifying which half is sorted and checking if the target lies within that sorted range.

### Algorithm Explanation
The algorithm works as follows:
1. Use standard binary search framework with left and right pointers
2. Calculate mid index
3. Determine which half is sorted:
   - If `nums[left] <= nums[mid]`, left half is sorted
   - Otherwise, right half is sorted
4. Check if target is in the sorted half:
   - If left half is sorted and `nums[left] <= target < nums[mid]`, search left
   - If right half is sorted and `nums[mid] < target <= nums[right]`, search right
   - Otherwise, search the other half

### Time and Space Complexity
- **Time Complexity**: O(log n) - Standard binary search with constant work at each step
- **Space Complexity**: O(1) - Only using a constant amount of extra space

### Example Walkthrough
For nums = [4,5,6,7,0,1,2], target = 0:
1. left=0, right=6, mid=3, nums[mid]=7
2. Left half [4,5,6,7] is sorted, but target 0 not in range [4,7]
3. Search right: left=4, right=6, mid=5, nums[mid]=1
4. Left half [0,1] is sorted, target 0 in range [0,1)
5. Search left: left=4, right=4, nums[mid]=0 == target, return 4

### Edge Cases Handled
- Single element array
- Target at beginning or end of array
- Target not present in array
- Array with two elements
- Target equals the pivot point or adjacent elements