class Solution(object):
    def judgeCircle(self, moves):
        l=r=u=d=0
        for i in range(len(moves)):
            if moves[i]=='L':
                l+=1
            elif moves[i]=='R':
                r+=1
            elif moves[i]=='U':
                u+=1
            elif moves[i]=='D':
                d+=1
        return l == r and u == d
        