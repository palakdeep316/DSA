class Solution(object):
    def countConsistentStrings(self, allowed, words):
        sum=0
        for i in words:
            valid=True
            for j in range(len(i)):
                if i[j] not in allowed:
                    valid=False
            if valid:
                sum+=1
        return sum   