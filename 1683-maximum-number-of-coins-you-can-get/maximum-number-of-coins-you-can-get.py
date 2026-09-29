class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        ans=0
        n=len(piles)
        for i in range(n-2,n//3-1,-2):
            ans+=piles[i]
        return ans