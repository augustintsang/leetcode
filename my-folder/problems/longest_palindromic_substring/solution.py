class Solution:
    def longestPalindrome(self, s: str) -> str:        
        result = ""
        for i in range(len(s)):
            l = i
            r = i
            while l-1 in range(len(s)) and s[l-1] == s[i]:
                l -= 1
            while r+1 in range(len(s)) and s[r+1] == s[i]:
                r += 1
            while l-1 in range(len(s)) and r+1 in range(len(s)) and s[r+1] == s[l-1]:
                r+=1
                l-=1
            
            curr = s[l:r+1]
            if len(curr) > len(result):
                result = curr
        return result
            

            
        
        