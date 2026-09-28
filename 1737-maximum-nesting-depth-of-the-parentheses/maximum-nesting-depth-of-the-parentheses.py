class Solution(object):
    def maxDepth(self, s):
        sol=count=0
        for i in range (len(s)):
            if s[i]=="(":
                count+=1
            if s[i]==")":
                sol=max(sol,count)
                count-=1
        return sol
            