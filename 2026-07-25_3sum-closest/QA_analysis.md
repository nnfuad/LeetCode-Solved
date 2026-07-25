# 3Sum Closest

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/3sum-closest/

---


**Problem Understanding**: The task is to find three integers from distinct indices whose sum is closest to the target. The array length n satisfies 3 <= n <= 500. Each element nums[i] is between -1000 and 1000. The target is between -10^4 and 10^4. It is guaranteed that there is exactly one solution (i.e., a unique closest sum, though multiple triples might yield same sum? They say exactly one solution, but I think it means the answer is unique, not that there is a triple with exact match). The goal is to return that sum.

**Optimal Approach**: Sort the array in non-decreasing order. Then for each fixed element at index i (0 <= i <= n-3), use the two-pointer technique on the remaining subarray (i+1 .. n-1) to find the pair that, together with nums[i], gives a sum closest to target. This runs in O(n^2) time. Only O(1) extra space is required besides the sorting storage.

**Solution Steps**:
1. Sort the input array `nums`.
2. Initialize `closest_sum` to the sum of the first three elements and `min_diff` to its absolute difference from `target`.
3. Iterate over `i` from 0 to n-3 (inclusive):
   - Skip duplicates for `i` to reduce work (optional but good).
   - Set `left = i+1`, `right = n-1`.
   - While `left < right`:
     - Compute `current_sum = nums[i] + nums[left] + nums[right]`.
     - If `current_sum == target`, return `current_sum` immediately.
     - If `abs(current_sum - target) < min_diff`, update `min_diff` and `closest_sum`.
     - If `current_sum < target`, increment `left` (to increase the sum).
     - Else, decrement `right` (to decrease the sum).
4. After processing all i, return `closest_sum`.

**Complexity Analysis**:
- Time: Sorting O(n log n). For each i, the while loop runs O(n) in total across all left/right movements, giving O(n^2) overall. So total O(n^2).
- Space: O(1) extra (sorting may use O(log n) for recursion stack in Timsort, but generally considered O(1) or O(log n)). The input array is modified in place.

**Example Walkthrough**:
- **Example 1**: `nums = [-1,2,1,-4]`, `target = 1`.
  - After sorting: `[-4,-1,1,2]`.
  - `i=0` (value -4): `left=1` (-1), `right=3` (2) → sum = -3, diff=4. `closest_sum=-3`, `min_diff=4`. Since sum < target, left++ → left=2 (1). sum = -4+1+2 = -1, diff=2. Update `closest_sum=-1`, `min_diff=2`. sum < target, left++ → left=3, loop ends.
  - `i=1` (value -1): `left=2` (1), `right=3` (2) → sum = 2, diff=1. Update `closest_sum=2`, `min_diff=1`. sum > target, right-- → right=2, loop ends.
  - Result: `2`.
- **Example 2**: `nums = [0,0,0]`, `target = 1`.
  - Sorted: `[0,0,0]`.
  - `i=0` (0): `left=1`, `right=2` → sum=0, diff=1. `closest_sum=0`, `min_diff=1`. sum < target, left++ → left=2, loop ends.
  - Result: `0`.

**Key Insights**: Sorting enables the two-pointer technique to efficiently search for the optimal pair. When the sum is too low, moving the left pointer rightwards increases the sum; when too high, moving right leftwards decreases it. The algorithm naturally explores sums in a sorted order, ensuring that the closest sum is found without checking every combination.

**Conclusion**: The two-pointer approach after sorting is the standard solution for 3Sum Closest, delivering an optimal O(n^2) time and O(1) space complexity. It reliably handles all given constraints and passes typical test cases.
