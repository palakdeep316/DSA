class Solution(object):
    def maximumOddBinaryNumber(self, s):
        new=''
        count=0
        for i in range(len(s)):
            if s[i]=='1':
                new+='1'
            else:
                count+=1
        return new[:(len(s)-count)-1]+'0'*count+'1'