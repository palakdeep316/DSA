class Solution(object):
    def intersection(self, nums1, nums2):
        new=[]
        for i in nums1:
            for j in nums2:
                if i==j:
                    new.append(i)
        new= list(set(new))
        return new