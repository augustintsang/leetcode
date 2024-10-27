class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        l = 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l = l+1
            
            charSet.add(s[r])
            currLength = r - l + 1
            length = max(length, currLength)
        
        return length
