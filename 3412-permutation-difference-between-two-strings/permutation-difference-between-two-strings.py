class Solution(object):
    def findPermutationDifference(self, s, t):
        sum=0
        for i in range(len(s)):
            j=t.find(s[i])
            sum+=abs(i-j)
        return sum