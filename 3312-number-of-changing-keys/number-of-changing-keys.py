class Solution(object):
    def countKeyChanges(self, s):
        s=s.lower()
        cnt=0
        for i in range (1,len(s)):
            if s[i]!=s[i-1]:
                cnt+=1
        return cnt