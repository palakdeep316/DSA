class Solution(object):
    def prefixCount(self, words, pref):
        count=0
        for i in range(len(words)):
            if pref in words[i][:len(pref)]:
                count+=1
        return count