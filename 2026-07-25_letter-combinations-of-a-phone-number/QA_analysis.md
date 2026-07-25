# Letter Combinations of a Phone Number

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/letter-combinations-of-a-phone-number/

---

## Problem Analysis

### Understanding the Problem
We need to generate all possible letter combinations that a string of digits (2-9) could represent based on a standard telephone keypad mapping. Each digit maps to a specific set of letters:

- 2: "abc"
- 3: "def"
- 4: "ghi"
- 5: "jkl"
- 6: "mno"
- 7: "pqrs"
- 8: "tuv"
- 9: "wxyz"

### Examples
- Input: "23" → Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
- Input: "2" → Output: ["a","b","c"]

## Approach Selection

### Method: Backtracking (DFS)
This is a classic backtracking problem where we explore all possible combinations.

**Algorithm:**
1. Create a mapping of digits to their corresponding letters
2. Use recursive backtracking to build all combinations
3. At each step, pick a letter for the current digit and recurse for the next digit
4. When we've processed all digits, add the combination to the result

**Time Complexity:** O(3^N × 4^M × N)
- N: count of digits with 3 letters (2,3,4,5,6,8)
- M: count of digits with 4 letters (7,9)
- Each combination takes O(N) time to build

**Space Complexity:** O(3^N × 4^M × N)
- For storing all combinations in the result
- Recursion depth: O(N)

### Alternative: Iterative Approach
We could also solve this iteratively using breadth-first expansion:
1. Start with an empty string in a queue
2. For each digit, expand all existing combinations with its letters
3. Replace the queue with new combinations

Both approaches have similar complexity, but backtracking is more intuitive for this problem.