class Solution(object):
    def maxProduct(self, n):
        ans=[]
        while n!=0:
            d=n%10
            ans.append(d)
            n//=10
        ans.sort()
        return ans[-1]*ans[-2]