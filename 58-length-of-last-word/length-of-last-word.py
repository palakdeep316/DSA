class Solution(object):
    def lengthOfLastWord(self, s):
        a=s.strip()
        a=a.split(" ")
        return len(a[-1])