# Valid Sudoku

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/valid-sudoku/

---

### Problem Analysis
The problem requires validating a 9x9 Sudoku board according to three rules: rows, columns, and 3x3 sub-boxes must not contain duplicate digits (1-9). Empty cells ('.') are ignored. The challenge is to efficiently check all three constraints in a single pass.

### Optimal Approach
We use three arrays of sets to track digits seen in each row, column, and 3x3 sub-box. For each cell (i,j):
1. Skip if empty ('.')
2. Compute the sub-box index as `(i // 3) * 3 + (j // 3)`
3. Check if the digit exists in the corresponding row[i], column[j], or sub-box set. If found, return false.
4. Add the digit to all three sets.

### Time and Space Complexity
- **Time Complexity**: O(1) - The board size is fixed at 9x9, so we perform 81 iterations each with constant-time operations.
- **Space Complexity**: O(1) - We use 27 sets (9 rows + 9 columns + 9 boxes) each storing at most 9 elements.

### Solution Code
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == '.':
                    continue
                box_idx = (i // 3) * 3 + (j // 3)
                if c in rows[i] or c in cols[j] or c in boxes[box_idx]:
                    return False
                rows[i].add(c)
                cols[j].add(c)
                boxes[box_idx].add(c)
        return True
```