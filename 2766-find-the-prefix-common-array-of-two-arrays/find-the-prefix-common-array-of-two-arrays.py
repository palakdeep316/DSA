class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        pre=[]
        for i in range(len(A)):
            sum=0
            for j in range(i+1):
                if B[j] in A[:i+1]:
                    sum+=1
            pre.append(sum)
        return pre