# Count and Say

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/count-and-say/

---

The Count and Say problem requires generating a sequence where each term is derived from the previous one by applying run-length encoding. The key steps are:

1. **Understanding Run-Length Encoding**: Each consecutive group of identical digits in the previous term is replaced by the count followed by the digit itself. For example, '1211' becomes '111221' (one 1, one 2, two 1s).

2. **Iterative Approach**: Starting with the base case '1', iteratively build each subsequent term up to n. This is more efficient than recursion and aligns with the follow-up suggestion.

3. **Algorithm Execution**: For each term from 2 to n:
   - Traverse the current string to identify consecutive groups.
   - Construct the next string by appending the count and the respective digit for each group.

**Time and Space Complexity**:
- **Time Complexity**: O(n * k), where k is the length of the longest string generated. As each term can grow exponentially, k grows exponentially with n. For n=30, this is manageable given the problem constraints.
- **Space Complexity**: O(k), since we store only the current and next strings at each step.

**Edge Cases**: Handle n=1 directly. Ensure that the loop for run-length encoding correctly processes the last character group.

The solution correctly handles all cases and efficiently builds the sequence iteratively.