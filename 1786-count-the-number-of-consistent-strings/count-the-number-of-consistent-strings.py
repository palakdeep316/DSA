class Solution(object):
    def countConsistentStrings(self, allowed, words):
        sum=0
        for i in words:
            for j in range(len(i)):
                if i[j] not in allowed:
                    break
            else:
                sum+=1
        return sum        