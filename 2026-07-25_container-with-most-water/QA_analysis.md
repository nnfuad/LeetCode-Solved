# Container With Most Water

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/container-with-most-water/

---

# Problem Overview
The task is to find two vertical lines that, together with the x-axis, form a container that holds the maximum amount of water. Each line's height is given by the array `height`, and the container's area is `min(height[i], height[j]) * (j - i)`.

# Intuition
A brute-force check of all pairs yields O(n²) time, which is infeasible for the given constraints (n up to 10⁵). Instead, we can use a greedy two-pointer approach that scans the array in a single pass.

# Optimal Approach
Initialize two pointers, `left` at index 0 and `right` at index `n-1`. At each step, compute the current area using the shorter line. The key observation is that moving the pointer that points to the shorter line inward cannot discard a potentially better solution, because any area that uses that line with another pointer further away would have a larger width but no greater height (since the height is limited by that short line). Therefore, we move the shorter pointer inward and repeat until they meet. This process explores all promising candidates in O(n) time.

# Complexity Analysis
- **Time Complexity:** O(n) – each iteration reduces the distance between pointers by one.
- **Space Complexity:** O(1) – only a constant amount of extra memory is used.

# Correctness Proof
The algorithm maintains the invariant that the optimal pair must lie within the current subarray `[left, right]`. When `height[left] < height[right]`, for any `k` between `left+1` and `right`, the area formed by `left` and `k` cannot exceed `height[left] * (right-left)` because the width is smaller and the height is at most `height[left]`. Hence, `left` can never be part of the optimal solution when paired with any line to its right, so we advance `left`. The symmetric argument holds when `height[right] <= height[left]`. By induction, the algorithm finds the global maximum.

# Solution Code
The implementation follows the two-pointer logic described above.