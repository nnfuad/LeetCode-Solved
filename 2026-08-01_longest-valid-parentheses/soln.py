class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        Find the length of the longest valid parentheses substring.
        
        Args:
            s: A string containing only '(' and ')'
        
        Returns:
            Length of the longest valid (well-formed) parentheses substring
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not s:
            return 0
        
        # Stack to store indices of unmatched '(' characters
        # Initialize with -1 to serve as base for length calculations
        stack = [-1]
        max_length = 0
        
        for i, char in enumerate(s):
            if char == '(':
                # Push index of opening parenthesis
                stack.append(i)
            else:  # char == ')' 
                # Pop to try to match the closing parenthesis
                stack.pop()
                
                if not stack:
                    # No matching opening parenthesis, this becomes new base
                    stack.append(i)
                else:
                    # Found a valid pair, calculate length
                    current_length = i - stack[-1]
                    max_length = max(max_length, current_length)
        
        return max_length