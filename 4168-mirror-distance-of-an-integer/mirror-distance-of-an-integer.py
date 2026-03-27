class Solution(object):
    def mirrorDistance(self, n):
        m=str(n)
        m=m[::-1]
        m=int(m)
        return abs(n-m)