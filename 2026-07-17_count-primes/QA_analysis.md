# Count Primes

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/count-primes/

---

The problem requires counting the number of prime numbers less than a given integer n. The optimal approach is to use the Sieve of Eratosthenes algorithm, which efficiently marks non-prime numbers up to n. The Sieve works by iteratively marking the multiples of each prime starting from 2. The time complexity is O(n log log n), and the space complexity is O(n), which is feasible for n up to 5*10^6.

Key Steps:
1. Handle edge cases where n is 0 or 1, returning 0 immediately.
2. Initialize a boolean array `is_prime` of size n, marking all entries as True initially.
3. Mark positions 0 and 1 as non-prime (False).
4. For each number i from 2 to sqrt(n), if i is still marked as prime, mark all its multiples starting from i*i as non-prime.
5. Sum the True values in the `is_prime` array to get the count of primes less than n.

This approach ensures that we efficiently eliminate non-prime numbers and count the remaining primes.