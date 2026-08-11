# Combination Sum II

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/combination-sum-ii/

---

The problem requires finding all unique combinations of numbers from the 'candidates' list that sum to 'target', with each number used at most once. The solution must avoid duplicate combinations even if the input contains duplicates.  

**Approach**: 
1. **Sorting**: First, sort the candidates array. This helps in efficiently skipping duplicates and allows early termination when the current candidate exceeds the remaining target. 
2. **Backtracking**: Use a recursive backtracking approach to explore all possible combinations. The backtracking function will track the current combination, the start index (to avoid reusing previous elements), and the remaining target. 
3. **Duplicate Handling**: To avoid generating duplicate combinations, skip over candidates that are the same as the previous one at the same recursion level. This is done by checking if the current index is greater than the start index and the current candidate matches the previous one. 

**Key Modifications for Efficiency**: 
- Early termination: If adding the current candidate exceeds the remaining target, break the loop since the sorted array ensures all subsequent candidates will also exceed the target. 
- Skipping duplicates: When encountering a duplicate in the same loop iteration (level), skip it to avoid redundant paths. 

**Time Complexity**: O(2^N) in the worst case, where N is the number of candidates. However, pruning through sorting and duplicates reduces this in practice. 
**Space Complexity**: O(N) for the recursion stack and storing the current path.