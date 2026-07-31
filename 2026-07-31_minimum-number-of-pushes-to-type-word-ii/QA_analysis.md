# Minimum Number of Pushes to Type Word II

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

---

### Problem Understanding

The problem requires us to determine the minimum number of key presses needed to type a given string `word` on a telephone keypad, where we can remap the letters to keys 2-9 in any configuration. Each letter must be mapped to exactly one key, and the number of presses for a letter is its position on its assigned key. The goal is to minimize the total number of presses across all letters in `word`.

### Key Insights

1. **Frequency Matters**: The letters that appear more frequently in `word` should be assigned to the first position on their respective keys to minimize the number of presses. For instance, the most frequent letter should be assigned to the first position of some key (1 press), the next most frequent letters should also be assigned to first positions of other keys, and so on until all keys are filled with one letter each. Then, the next most frequent letters should be assigned to the second positions of keys, and so forth.

2. **Greedy Approach**: This is a classic problem that can be solved using a greedy algorithm. The optimal strategy involves sorting the letters by their frequencies in descending order and then assigning them to key positions in a way that the most frequent letters get the lowest number of presses.

3. **Mathematical Formulation**: If we have `k` keys (8 keys from 2-9), the first `k` most frequent letters will each cost 1 press. The next `k` letters will cost 2 presses each, the next `k` letters 3 presses, and so on.

### Algorithm Selection

1. **Count Frequencies**: First, count the frequency of each letter in `word`.
2. **Sort Frequencies**: Sort these frequencies in descending order.
3. **Calculate Total Presses**: For each letter, its contribution to the total is its frequency multiplied by its press count (1 for first `k` letters, 2 for next `k`, etc.).

### Solution Code

```python
from collections import defaultdict

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count the frequency of each character in the word
        freq = defaultdict(int)
        for char in word:
            freq[char] += 1
        
        # Sort the frequencies in descending order
        sorted_freq = sorted(freq.values(), reverse=True)
        
        total_presses = 0
        
        # Calculate the total presses
        for i, count in enumerate(sorted_freq):
            # Determine the number of presses for this character
            # It's (i // 8) + 1, because first 8 chars are press 1, next 8 press 2, etc.
            presses = (i // 8) + 1
            total_presses += presses * count
        
        return total_presses
```

### Complexity Analysis

- **Time Complexity**: O(n + m log m), where n is the length of `word` and m is the number of distinct letters in `word`. Counting frequencies is O(n), and sorting is O(m log m). Since m is at most 26 (letters in the English alphabet), the time complexity is effectively O(n).

- **Space Complexity**: O(1) or O(m), where m is the number of distinct letters. The space used for the frequency dictionary and the sorted list is O(m), which is constant (<= 26).

### Explanation of the Solution

1. **Frequency Counting**: We use a dictionary to count how often each letter appears in `word`. This step ensures we know which letters are most frequent.
2. **Sorting**: By sorting the frequencies in descending order, we prioritize the most frequent letters for the least number of presses.
3. **Press Calculation**: The press count for each letter is determined by its position in the sorted list. The first 8 letters get 1 press, the next 8 get 2, and so on. We sum the product of each letter's frequency and its press count to get the total minimum presses required.

This approach efficiently minimizes the total presses by leveraging the greedy strategy of assigning the lowest press counts to the most frequent letters.