class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Handle the case where either number is zero
        if num1 == "0" or num2 == "0":
            return "0"
        
        n1, n2 = len(num1), len(num2)
        # Result can be at most n1 + n2 digits
        result = [0] * (n1 + n2)
        
        # Multiply each digit and accumulate in result
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                # Convert char to digit
                d1 = ord(num1[i]) - ord('0')
                d2 = ord(num2[j]) - ord('0')
                
                # Positions in result array
                pos1 = i + j
                pos2 = i + j + 1
                
                # Multiply and add to existing value
                mul = d1 * d2
                total = mul + result[pos2]
                
                # Update positions with carry
                result[pos2] = total % 10
                result[pos1] += total // 10
        
        # Convert result array to string
        # Skip leading zeros
        start = 0
        while start < len(result) and result[start] == 0:
            start += 1
        
        return ''.join(str(d) for d in result[start:])