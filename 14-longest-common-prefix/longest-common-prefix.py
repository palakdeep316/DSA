class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        pre=strs[0]
        for i in range(1,len(strs)):
            while strs[i].find(pre) != 0:
                pre = pre[:-1]
                if pre == "":
                    return ""
        return pre