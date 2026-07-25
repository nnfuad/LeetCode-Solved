# Palindrome Number

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/palindrome-number/

---

A comprehensive markdown-formatted discussion of the problem, optimal approach (time and space complexity), and the solution.

**Problem Analysis**: The problem is to determine if a given integer x is a palindrome. A palindrome reads the same forward and backward. Constraints: x is in the range [-2^31, 2^31-1]. Negative numbers are not palindromes because the '-' sign appears only at the left. Additionally, numbers ending with 0 (except 0 itself) are not palindromes because reversing would introduce a leading zero. The solution must avoid converting the integer to a string.

**Optimal Approach**: To solve without string conversion, we reverse only half of the number and compare. Steps:
1. If x < 0 or (x % 10 == 0 and x != 0), return false.
2. Initialize rev = 0.
3. While x > rev: rev = rev * 10 + x % 10; x //= 10.
4. At the end, the number is a palindrome if x == rev (even digits) or x == rev // 10 (odd digits).
5. Return the condition.

**Complexity Analysis**: Time complexity is O(log10(x)) as we process roughly half the digits. Space complexity is O(1).

**Edge Cases**: x = 0 → true; x = -121 → false; x = 10 → false; x = 12321 → true; x = 1001 → true; x = 100 → false.

**Follow-up**: The described solution meets the follow‑up requirement by not using a string conversion.