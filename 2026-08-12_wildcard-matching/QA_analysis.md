# Wildcard Matching

**Difficulty:** Hard

**Link:** https://leetcode.com/problems/wildcard-matching/

---

The problem requires implementing a wildcard pattern matching function with support for '?' (matches any single character) and '*' (matches any sequence of characters, including empty). The matching must cover the entire input string.

### Approach:
Dynamic Programming (DP) is suitable here due to overlapping subproblems and optimal substructure. We define `dp[i][j]` as whether the first `i` characters of `s` match the first `j` characters of `p`. The key transitions are:

1. **Base Case**: `dp[0][0] = True` (empty pattern matches empty string).
2. **Initialization for `i=0`**: For the first row (empty string `s`), `dp[0][j]` is `True` only if all previous pattern characters are `*`.
3. **Transitions**:
   - If `p[j-1]` matches `s[i-1]` or is `?`, then `dp[i][j] = dp[i-1][j-1]`.
   - If `p[j-1]` is `*`, then `dp[i][j] = dp[i][j-1]` (matching zero chars) OR `dp[i-1][j]` (matching one or more chars).

### Space Optimization:
We use a 1D DP array (`prev_dp` and `curr_dp`) to reduce space complexity from `O(N*M)` to `O(M)`, where `N` is the length of `s` and `M` is the length of `p`.

### Complexity:
- **Time Complexity**: `O(N*M)` where `N` and `M` are lengths of `s` and `p`, respectively.
- **Space Complexity**: `O(M)` using two 1D arrays of size `M+1`.

### Edge Cases Handled:
- Empty `s` with all-`*` patterns.
- Patterns with mixed `*` and other characters.
- Direct matches without wildcards.
