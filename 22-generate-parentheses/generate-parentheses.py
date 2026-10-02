class Solution(object):
    def generateParenthesis(self, n):
        p=[]
        def backtrack(s,open,close):
            if open==n and close==n:
                p.append(s)
                return
            if open<n:
                backtrack(s+"(",open+1,close)
            if close<open:
                backtrack(s+")",open,close+1)
        backtrack("",0,0)
        return p