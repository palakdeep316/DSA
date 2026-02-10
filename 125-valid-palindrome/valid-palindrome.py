class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        new=""
        for i in range (len(s)):
            if s[i].isalnum():
                new+=s[i]
        return new == new[::-1]