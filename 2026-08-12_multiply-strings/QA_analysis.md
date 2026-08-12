# Multiply Strings

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/multiply-strings/

---

# Multiply Strings - Problem Analysis

## Problem Understanding
We need to multiply two non-negative integers represented as strings and return their product as a string. The key constraint is that we cannot use built-in BigInteger libraries or convert the inputs directly to integers.

## Approach: Simulating Manual Multiplication
This problem can be solved by simulating the multiplication process we learn in school. The key insight is:

1. When multiplying two numbers, each digit from the first number multiplies each digit from the second number
2. The result of multiplying digit at position$i$ (from right) of num1 with digit at position$j$ (from right) of num2 contributes to positions at indices $i+j$ and $i+j+1$ in the result (due to carry)
3. The maximum length of the product is at most $len(num1) + len(num2)$

## Algorithm
```
1. If either number is "0", return "0"
2. Create an array of size (len(num1) + len(num2)) initialized to 0
3. For each digit i in num1 (right to left):
   For each digit j in num2 (right to left):
     - Compute product = digit1 * digit2
     - pos1 = i + j (higher position)
     - pos2 = i + j + 1 (lower position)
     - total = product + result[pos2]
     - result[pos2] = total % 10
     - result[pos1] += total // 10
4. Convert result array to string, skipping leading zeros
```

## Complexity Analysis
- **Time Complexity**: O(n1 × n2) where n1 and n2 are the lengths of num1 and num2 respectively. This is because we have nested loops iterating over all pairs of digits.
- **Space Complexity**: O(n1 + n2) for storing the result array.

## Edge Cases Handled
- Multiplication by zero
- Numbers with leading zeros (though constraint says no leading zeros except for "0")
- Very large numbers (up to 200 digits each)

## Correctness Proof
The simulation correctly mimics the standard multiplication algorithm:
- The position mapping ($i+j$ and $i+j+1$) correctly accounts for place values (units, tens, hundreds, etc.)
- Carry propagation ensures each position holds a single digit
- The final conversion to string correctly represents the numeric result