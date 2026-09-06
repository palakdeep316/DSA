class Solution(object):
    def smallestNumber(self, n, t):
        while True:
            num=n
            mul=1
            while num!=0:
                d=num%10
                mul*=d
                num//=10
            if mul%t==0:
                return n
            n+=1