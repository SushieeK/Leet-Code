class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        freqs = [0] * 128
        
        for c in s:
            freqs[ord(c)] += 1
        
        ans, odd = 0, 0
        for freq in freqs:
            ans += freq & (~1)
            odd |= freq & 1
        
        return ans + odd