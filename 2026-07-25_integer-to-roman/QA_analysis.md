# Integer to Roman

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/integer-to-roman/

---

The problem requires converting an integer to a Roman numeral, which involves understanding the subtractive notation rules and the order of symbol values. The optimal approach is a greedy algorithm that iterates through a predefined list of value-symbol pairs in descending order. For each pair, we repeatedly subtract the value from the input number and append the corresponding symbol until the number is reduced to zero. This ensures that we always use the largest possible values first, adhering to Roman numeral construction rules.

Time Complexity: O(1) - The loop runs a constant number of times (13 iterations), and each iteration's inner loop runs at most 3 times (for symbols like 'M' and 'I').

Space Complexity: O(1) - The output string length is bounded by a small constant (maximum length is 15 characters for any input up to 3999).

The solution leverages the predefined list of value-symbol pairs that includes all necessary subtractive forms (e.g., 4 as 'IV', 9 as 'IX'), allowing the algorithm to handle all valid inputs efficiently.