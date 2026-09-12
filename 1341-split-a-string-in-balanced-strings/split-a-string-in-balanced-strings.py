class Solution(object):
    def balancedStringSplit(self, s):
        count=0
        ans=0
        for ch in s:
            if ch=="L":
                count+=1
            else:
                count-=1
            if count==0:
                ans+=1
        return ans