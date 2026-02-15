class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        result=result2=''
        for i in word1:
            result+=i
        for i in word2:
            result2+=i
        if result==result2:
            return True
        else:
            return False