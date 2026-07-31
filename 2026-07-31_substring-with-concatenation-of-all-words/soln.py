class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_length = len(words[0])
        total_words = len(words)
        total_length = word_length * total_words
        n = len(s)
        
        if n < total_length:
            return []
        
        from collections import Counter
        target_count = Counter(words)
        result = []
        
        # Try each possible starting offset
        for offset in range(word_length):
            left = offset
            right = offset
            window_count = Counter()
            
            while right + word_length <= n:
                word = s[right:right + word_length]
                right += word_length
                
                if word in target_count:
                    window_count[word] += 1
                    
                    # Shrink window if count exceeds target
                    while window_count[word] > target_count[word]:
                        left_word = s[left:left + word_length]
                        window_count[left_word] -= 1
                        left += word_length
                    
                    # Check if window has correct size
                    if (right - left) == total_length:
                        result.append(left)
                else:
                    # Reset window
                    window_count.clear()
                    left = right
        
        return result