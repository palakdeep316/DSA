class Solution(object):
    def smallestEvenMultiple(self, n):
        i=1
        while(i<=(n*2)):
            if (i%n==0) and (i%2==0):
                return i
            i+=1        