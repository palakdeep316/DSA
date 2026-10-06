class Solution(object):
    def minAddToMakeValid(self, s):
        ans=0
        score=0
        for i in range (len(s)):
            if s[i]=='(':
                score+=1   
            else:
                if score>0:
                    score-=1
                else:
                    ans+=1
        return ans+score