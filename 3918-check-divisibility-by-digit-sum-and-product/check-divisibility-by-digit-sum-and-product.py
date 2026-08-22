class Solution(object):
    def checkDivisibility(self, n):
        dsum=0
        dmul=1
        num=n
        while num>0:
            dsum+=num%10
            dmul*=num%10
            num//=10
        if n%(dsum+dmul)==0:
            return True
        else:
            return False