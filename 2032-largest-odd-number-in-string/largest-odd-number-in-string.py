class Solution(object):
    def largestOddNumber(self, num):
        ans=0
        if int(num)%2!=0:
            return num
        else:
            sub=''
            for i in range(len(num)):
                s=int(num[i])
                if s%2!=0:
                    sub = num[:i+1]
        return sub