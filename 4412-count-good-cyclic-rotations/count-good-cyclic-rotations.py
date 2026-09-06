class Solution(object):
    def countGoodRotations(self, nums):
        ans=0
        s1=s2=0
        half=len(nums)/2
        s1=sum(nums[:half])
        s2=sum(nums[half:])
        for i in range(len(nums)):
            if s1>s2:
                ans+=1
            s1+=nums[(i+half)%len(nums)]-nums[i]
            s2+=nums[i]-nums[(i+half)%len(nums)]
        return ans