class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        result=[]
        minimum=float('inf')
        for i in range(1,len(arr)):
            mini=(arr[i]-arr[i-1])
            minimum=min(minimum,mini)
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == minimum:
                result.append([arr[i-1], arr[i]])
        return result