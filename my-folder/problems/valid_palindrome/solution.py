class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = ""
        reverse = ""
        for i in range(len(s) -1, -1, -1):
            if s[i].isalnum():
                reverse = reverse + s[i].lower()
                forward = s[i].lower() + forward
        if reverse == forward:
            return True
        else:
            return False
