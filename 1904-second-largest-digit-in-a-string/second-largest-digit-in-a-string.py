class Solution(object):
    def secondHighest(self, s):
        lt=[]
        for i in range (len(s)):
            if s[i].isdigit():
                lt.append(s[i])
        lt= list(set(lt))
        lt.sort()
        if len(lt)<2:
            return -1
        return int((lt[-2]))
        