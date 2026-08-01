# Sudoku Solver

**Difficulty:** Hard

**Link:** https://leetcode.com/problems/sudoku-solver/

---

The problem requires solving a Sudoku puzzle by filling empty cells (denoted by '.') such that each row, column, and 3x3 sub-box contains digits 1-9 exactly once. A backtracking approach is optimal here. We track existing numbers in rows, columns, and boxes using sets for O(1) validity checks. For each empty cell, we try numbers 1-9, placing valid ones and recursively proceeding. If dead-end, backtrack. The worst-case time complexity is O(9^(n)) where n is empty cells, but constraints prune the search space. Space complexity is O(81) for tracking sets. The code initializes sets for rows, columns, and boxes, then uses a nested helper for backtracking recursion to fill the board in-place.