class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        s = '1'
        for _ in range(2, n + 1):
            next_s = []
            count = 1
            current_char = s[0]
            for j in range(1, len(s)):
                if s[j] == current_char:
                    count += 1
                else:
                    next_s.append(str(count))
                    next_s.append(current_char)
                    current_char = s[j]
                    count = 1
            next_s.append(str(count))
            next_s.append(current_char)
            s = ''.join(next_s)
        return s