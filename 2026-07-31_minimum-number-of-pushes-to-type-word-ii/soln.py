class Solution:
    def minimumPushes(self, word):
        from collections import defaultdict
        freq = defaultdict(int)
        for char in word:
            freq[char] += 1
        
        sorted_freq = sorted(freq.values(), reverse=True)
        
        total_presses = 0
        
        for i, count in enumerate(sorted_freq):
            presses = (i // 8) + 1
            total_presses += presses * count
        
        return total_presses