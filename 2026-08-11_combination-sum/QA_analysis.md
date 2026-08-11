# Combination Sum

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/combination-sum/

---

The problem requires finding all unique combinations of distinct integers from a given array where the sum equals a target. Each number can be used an unlimited number of times, but combinations are considered unique based on the frequency of numbers (order doesn't matter). 

Optimal Approach:

The problem can be efficiently solved using a backtracking approach. The key insight is to explore all possible combinations by recursively adding candidates and pruning branches where the sum exceeds the target. To avoid duplicates, we enforce a non-decreasing order in combinations by only considering candidates starting from the current index. This ensures each combination is built in a canonical order, preventing permutations like [2,3] and [3,2] from being counted as separate cases.

Steps:
1. Sort the candidates to facilitate early termination when the current candidate exceeds the remaining target.
2. Use a recursive backtracking function that tracks the current combination (path), the remaining target, and the starting index.
3. For each step from the current start index:
- If the candidate is greater than the remaining target, break the loop (since further candidates will also be larger).
- Add the candidate to the path and recursively call backtracking with the same index (to allow reuse).
- After returning from recursion, backtrack by removing the candidate from the path.

Time Complexity: O(N^ (T/M)), where N is the number of candidates, T is the target, and M is the minimal candidate value. This is because each candidate can be chosen multiple times up to T/M times.

Space Complexity: O(T/M) for the recursion stack depth. The output storage is proportional to the number of valid combinations, which is constrained to be under 150 per the problem statement.

This approach efficiently explores all valid combinations while avoiding duplicates through controlled iteration and pruning.