# Mirror Reflection

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/mirror-reflection/

---

The problem involves a laser bouncing in a square room with mirrors on all walls. The goal is to determine which receptor (numbered 0, 1, or 2) the laser hits first. The key insight is to model the reflections as extending the room into a grid of mirrored rooms, allowing the laser's path to be treated as a straight line. The solution involves calculating the greatest common divisor (GCD) of p and q to determine the parity of the number of reflections in each direction.

**Approach**:
1. Compute the GCD of p and q, denoted as d.
2. Calculate m = p / d and n = q / d. These represent the number of room widths and heights needed for the laser to align with a corner in the grid.
3. Determine the receptor based on the parity of m and n:
   - If m is even and n is odd, return 2 (southeast corner).
   - If m is odd and n is even, return 0 (northeast corner).
   - If both are odd, return 1 (northwest corner).

**Time Complexity**: O(log(min(p, q))) due to the GCD computation using the Euclidean algorithm.
**Space Complexity**: O(1) as no additional space is used beyond a few variables.

The solution leverages mathematical properties of GCD and modular arithmetic to efficiently determine the first receptor hit without simulating reflections.