class Solution(object):
    def garbageCollection(self, garbage, travel):
        total=0
        for house in garbage:
            total+=len(house)
        for i in range(1,len(travel)):
            travel[i]+=travel[i-1]
        for g in ['M','P','G']:
            for i in range(len(garbage)-1,-1,-1):
                if g in garbage[i]:
                    total+=travel[i-1] if i>0 else 0
                    break
        return total