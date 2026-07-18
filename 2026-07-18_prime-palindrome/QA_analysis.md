# Prime Palindrome

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/prime-palindrome/

---

## Problem Analysis

**Problem Statement:** Find the smallest prime palindrome greater than or equal to a given integer n.

**Key Definitions:**
- **Prime:** An integer with exactly two divisors (1 and itself). Note: 1 is not prime.
- **Palindrome:** An integer that reads the same forwards and backwards.
- **Prime Palindrome:** An integer that is both prime and a palindrome.

**Key Observations:**

1. **Even-Length Palindrome Property:** All palindromes with an even number of digits are divisible by 11. This is a crucial mathematical insight that dramatically reduces the search space.

   *Proof sketch:* For a 2k-digit palindrome, the number can be expressed as sum of terms where each term (10^i + 10^(2k-1-i)) for even positions is divisible by 11.

2. **Search Space Reduction:** We only need to check:
   - Single-digit primes: 2, 3, 5, 7
   - The palindrome 11
   - Odd-length palindromes (length >= 3)

3. **Palindrome Generation:** An odd-length palindrome is uniquely determined by its first half (including the middle digit). For example:
   - Length 3: prefix "12" → palindrome "121"
   - Length 5: prefix "123" → palindrome "12321"

**Algorithm Design:**

1. Handle edge cases for n ≤ 11 directly
2. Generate odd-length palindromes ≥ n in increasing order
3. For each palindrome, check if it's prime using optimized trial division
4. Return the first prime palindrome found

**Time Complexity:**
- Let k be the number of digits. We generate O(10^(k/2)) palindromes.
- Each primality check is O(√p) = O(10^(k/2)).
- Total: O(10^(k)) in the worst case, but practically much faster due to prime density.
- For n ≤ 10^8, this is efficient enough.

**Space Complexity:** O(1) - we only use a constant amount of extra space.

**Optimizations Applied:**

1. Skip even-length palindromes entirely (they're divisible by 11)
2. Use 6k±1 optimization for primality testing
3. Generate palindromes directly rather than checking every number
4. Handle small cases (n ≤ 11) with a simple lookup

**Edge Cases Considered:**
- n itself is a prime palindrome (should return n)
- n is small (≤ 11)
- n requires checking multiple palindromes before finding a prime
