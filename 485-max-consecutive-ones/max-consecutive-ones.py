class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count=[0]
        con=0
        for i in range(len(nums)):
            if nums[i]==1:
                con+=1
            else:
                count.append(con)
                con=0
        count.append(con)
        return max(count)