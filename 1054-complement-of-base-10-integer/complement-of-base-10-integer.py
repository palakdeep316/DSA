class Solution(object):
    def bitwiseComplement(self, n):
        s=''
        n=bin(n)[2:]
        for i in range (len(n)):
            if n[i]=='1':
                s+='0'
            else:
                s+='1'
        return int(s,2)