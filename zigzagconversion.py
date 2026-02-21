class Solution:
    def convert(self, s, numRows):
        # If only 1 row or string is small, no zigzag needed
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create empty rows
        rows = [""] * numRows
        
        current_row = 0
        going_down = False
        
        for char in s:
            # Add character to current row
            rows[current_row] += char
            
            # Change direction at top or bottom
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move up or down
            if going_down:
                current_row += 1
            else:
                current_row -= 1
        
        # Join all rows
        return "".join(rows)