# Regular Expression Matching

**Difficulty:** Hard

**Link:** https://leetcode.com/problems/regular-expression-matching/

---

The problem requires implementing regular expression matching with support for '.' and '*' where '.' matches any single character and '*' matches zero or more of the preceding element. The solution must determine if the entire input string matches the pattern.

### Approach
The optimal approach uses **Dynamic Programming (DP)** to efficiently solve the problem with overlapping subproblems and optimal substructure. The DP table `dp[i][j]` represents whether the first `i` characters of the string `s` match the first `j` characters of the pattern `p`.

#### Key Steps:
1. **Initialization**: Create a DP table of size `(m+1) x (n+1)` where `m` and `n` are the lengths of `s` and `p` respectively. Set `dp[0][0] = True` since an empty string matches an empty pattern.
2. **First Row Handling**: For patterns with '*' (which can match zero occurrences), fill the first row (empty string) by checking if the pattern up to `j-2` can also match an empty string.
3. **DP Transitions**:
   - **Non-'*' Character**: If the current pattern character is not '*', check if it matches the current string character (directly or via '.') and update `dp[i][j]` based on `dp[i-1][j-1]`.
   - **'*' Character**: Handle two cases:
     - Zero occurrences: Use `dp[i][j-2]`.
     - One or more occurrences: Check if the preceding pattern character matches the current string character and use `dp[i-1][j]`.
4. **Result**: Return `dp[m][n]` indicating if the entire string matches the pattern.

#### Complexity
- **Time Complexity**: O(m * n) where `m` and `n` are the lengths of `s` and `p`. Each cell in the DP table is computed once.
- **Space Complexity**: O(m * n) for storing the DP table.

### Edge Cases
- Empty string with patterns containing '*' (e.g., `s = ""`, `p = "a*"` → True).
- Patterns requiring zero occurrences (e.g., `s = "ab"`, `p = ".*c"` → False).
- Consecutive '*' patterns (e.g., `s = "a"`, `p = "ab*"` → True).

### Solution Code
The Python implementation uses a 2D DP array with proper initialization and transitions as described above.