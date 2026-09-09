class Solution(object):
    def countCommas(self, n):
        total=0
        x=1000
        com=1
        while x<=n:
            total+=(min(n,x*1000-1)-x+1)*com
            x*=1000
            com+=1
        return total