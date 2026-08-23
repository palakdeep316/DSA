class Solution(object):
    def brokenCalc(self, startValue, target):
        result=0
        while target > startValue:
            if target % 2 != 0:
                target += 1
            else:
                target //= 2
            result += 1
        return result + (startValue - target)