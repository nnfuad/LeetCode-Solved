class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Convert string to zigzag pattern and read line by line.
        
        Args:
            s: Input string to convert
            numRows: Number of rows in zigzag pattern
            
        Returns:
            Converted string read row by row
        """
        # Edge case: single row or empty string
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize rows as list of strings
        rows = [''] * numRows
        
        # Track current row and direction
        current_row = 0
        direction = 1  # 1 for down, -1 for up
        
        # Place each character in appropriate row
        for char in s:
            rows[current_row] += char
            
            # Change direction at boundaries
            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1
            
            current_row += direction
        
        # Concatenate all rows
        return ''.join(rows)