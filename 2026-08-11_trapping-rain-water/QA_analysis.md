# Trapping Rain Water

**Difficulty:** Hard

**Link:** https://leetcode.com/problems/trapping-rain-water/

---

### Analysis

**Problem Understanding:**
The problem requires calculating the amount of trapped rainwater given an elevation map represented as an array of non-negative integers. Water can only be trapped between two bars if there are higher bars on both sides, and the amount trapped at each position is determined by the minimum of the highest bars to the left and right minus the height of the current bar.

**Optimal Approach - Two Pointers:**
The optimal solution uses a two-pointer approach with O(n) time complexity and O(1) space complexity. This approach leverages the observation that the amount of water trapped at any position depends on the minimum of the maximum heights from both directions.

**Key Steps:**
1. **Initialize Pointers & Variables:** Use two pointers (`left` and `right`) starting at the ends of the array. Track `left_max` and `right_max` to store the maximum heights encountered from the left and right ends, respectively. Initialize `result` to accumulate the total trapped water.
2. **Pointer Movement Decision:** Compare the current heights at `left` and `right` pointers. Move the pointer pointing to the shorter bar because the taller bar determines the water level constraint for the shorter side.
3. **Update Max Heights:** If the current height is greater than the respective max, update the max height. Otherwise, calculate the trapped water (min of left/right max minus current height) and add it to the result.
4. **Termination:** The loop continues until the pointers meet, ensuring all positions are processed.

**Time & Space Complexity:**
- **Time Complexity:** O(n) since each element is traversed once.
- **Space Complexity:** O(1) as we only use a few variables for pointers and max heights.

**Why It Works:**
By always moving the pointer with the shorter height, we ensure that the trapped water calculation for each position is correctly limited by the minimum of the two maximum heights. This approach avoids the need for precomputing arrays for maximum heights, achieving optimal space efficiency while maintaining linear time.