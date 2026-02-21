class Solution(object):
    def selfDividingNumbers(self, left, right):
        n=[]
        for i in range(left,right+1):
            a=True
            temp=i
            while (temp>0):
                d=temp%10
                if d==0 or i%d!=0:
                    a=False
                    break
                temp//=10
            if a:
                n.append(i)
        return n