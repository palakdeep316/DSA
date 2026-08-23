class Solution(object):
    def isPalindromic(self, s):
        b='0'
        ans=False
        for i in range(len(s)):
            new=0
            new+=ord(s[i])
            new=bin(new)
            b+=str(new[2:])
        if b==b[::-1]:
            ans=True
        return ans