class Solution(object):
    def maxFreqSum(self, s):
        vow=con=0
        v='aioue'
        for i in range(len(s)):
            fv=0
            fc=0
            if s[i] in v:
                fv=s.count(s[i])
            else:
                fc=s.count(s[i])
            if fv>vow:
                vow=fv
            elif fc>con:
                con=fc
        return vow+con