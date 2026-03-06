class Solution(object):
    def checkOnesSegment(self, s):
        for i in range (1,len(s)):
            if (s[i-1]=='0') and (s[i]=='1'):
                return False
        return True    