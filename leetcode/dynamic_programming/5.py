class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2: return s
        start = 0
        end = 0
        
        for i in range(n):
            len1 = self.expandAroundCenter(s,i,i)
            len2 = self.expandAroundCenter(s,i,i+1)
            max_len = max(len1,len2)
            if max_len > end - start:
                if len1 > len2:
                    start = i -int((len1-1)/2)
                    end = i + int((len1-1)/2)
                else:
                    start = i - int(len2/2 - 1)
                    end = i + int(len2/2)
                    
        return s[start:end+1]
        
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
            left -= 1
            right += 1
        return right-left-1
