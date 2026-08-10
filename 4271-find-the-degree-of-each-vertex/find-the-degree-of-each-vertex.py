class Solution(object):
    def findDegrees(self, matrix):
        for i in range(len(matrix)):
            matrix[i]=sum(matrix[i])
        return matrix                            