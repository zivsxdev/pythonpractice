

class Solution:
    def longestPalindrome(self, s):
        
        # If string is empty or single character
        if len(s) < 2:
            return s
        
        start = 0   # starting index of longest palindrome
        max_len = 1 # length of longest palindrome
        
        # Function to expand from center
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1
        
        for i in range(len(s)):
            
            # Check odd length palindrome
            l1, r1 = expand(i, i)
            
            # Check even length palindrome
            l2, r2 = expand(i, i + 1)
            
            # Compare lengths
            if r1 - l1 + 1 > max_len:
                start = l1
                max_len = r1 - l1 + 1
            
            if r2 - l2 + 1 > max_len:
                start = l2
                max_len = r2 - l2 + 1
        
        return s[start:start + max_len]
