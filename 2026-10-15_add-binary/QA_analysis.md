# Add Binary

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/add-binary/

---

The problem requires adding two binary strings and returning the result as a binary string. Binary addition is similar to decimal addition but with a base of 2, meaning each digit can only be 0 or 1, and carrying over occurs when the sum exceeds 1.\n\n### Approach\nThe optimal approach involves simulating the binary addition process:\n1. Start from the least significant bit (end of both strings).\n2. Sum the corresponding bits along with any carry from the previous step.\n3. The current digit of the result is (sum % 2), and the new carry is (sum // 2).\n4. Continue until all bits from both strings and the carry are processed.\n5. Reverse the result to get the correct order.\n\n### Time Complexity\nO(max(n, m)), where n and m are the lengths of the binary strings a and b, respectively. We process each bit of both strings once.\n\n### Space Complexity\nO(max(n, m)) for storing the result, which could be at most one bit longer than the longer input string.