class Solution(object):
    def mostWordsFound(self, sentences):
        max=0
        for i in sentences:
            a=i.count(" ")
            if max<=(a+1):
                max=a+1
        return max