class Solution(object):
    def maxDistinct(self, s):
        s=set(list(s))
        return len(s)   