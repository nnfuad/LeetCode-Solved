# Median of Two Sorted Arrays

**Difficulty:** Hard

**Link:** https://leetcode.com/problems/median-of-two-sorted-arrays/

---

## Problem Analysis

### Understanding the Problem
We need to find the median of two sorted arrays with O(log(m+n)) time complexity. The median is the middle value(s) of a sorted array - either a single middle element (odd length) or the average of two middle elements (even length).

### Key Insights
1. **Direct Merge Approach**: Merging both arrays and finding median takes O(m+n) time, which doesn't meet the requirement.
2. **Binary Search Insight**: We can use binary search on the smaller array to find a 'partition point' where:
   - Elements on the left side of the partition are all <= elements on the right side
   - The partition divides the combined array into two equal halves
3. **Partition Strategy**: If we partition nums1 at index p and nums2 at index q, we need:
   - p + q = (m + n + 1) / 2 (left half size)
   - max(nums1[p-1], nums2[q-1]) <= min(nums1[p], nums2[q])

### Algorithm
1. Ensure nums1 is the smaller array for efficiency
2. Binary search on nums1 to find the correct partition
3. Calculate corresponding partition in nums2
4. Validate partition and adjust search range
5. Calculate median based on partition boundaries

### Time & Space Complexity
- **Time**: O(log(min(m,n))) = O(log(m+n)) - meets requirement
- **Space**: O(1) - only using constant extra space

### Edge Cases Handled
- Empty arrays (one or both)
- Arrays of different lengths
- Negative numbers
- Single element arrays
