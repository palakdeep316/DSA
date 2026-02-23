class Solution(object):
    def scoreOfString(self, s):
        num=[]
        for i in range(1,len(s)):
            num.append(abs(ord(s[i-1])-ord(s[i])))
        return sum(num)