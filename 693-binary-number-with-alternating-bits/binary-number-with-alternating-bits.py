class Solution(object):
    def hasAlternatingBits(self, n):
        n=bin(n)[2:]
        for i in range(1,len(n)):
            if (n[i]=='0' and n[i-1]=='1')or(n[i]=='1' and n[i-1]=='0'):
                continue
            else:
                return False
        return True