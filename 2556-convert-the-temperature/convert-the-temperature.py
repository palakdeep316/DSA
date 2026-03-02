class Solution(object):
    def convertTemperature(self, celsius):
        l=[]
        l.append(celsius+273.15)
        l.append(celsius * 1.80 + 32.00)
        return (l)        