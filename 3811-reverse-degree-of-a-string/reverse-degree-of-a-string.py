class Solution(object):
    def reverseDegree(self, s):
        sum=0
        num=71
        for i in range(len(s)):
            rev=123-ord(s[i])
            sum+=(rev*(i+1))
        return sum