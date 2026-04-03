class Solution(object):
    def convertDateToBinary(self, date):
        date=date.split('-')
        new=[]
        for i in range (len(date)):
            date[i]=bin(int(date[i]))[2:]
            new.append(date[i])
        return '-'.join(new)