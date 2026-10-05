class Solution(object):
    def scoreOfParentheses(self, s):
        score=ans=0
        for i in range(len(s)):
            if s[i]=='(':
                ans+=1
            else:
                ans-=1
                if s[i-1]=='(':
                    score+=2**ans
        return score