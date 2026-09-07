class Solution(object):
    def duplicateZeros(self, arr):
        new=[]
        for i in range(len(arr)):
            new.append(arr[i])
            if arr[i]==0:
                new.append(0)
        for i in range(len(arr)):
            arr[i]=new[i]
        return arr