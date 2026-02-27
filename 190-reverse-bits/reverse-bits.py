class Solution(object):
    def reverseBits(self, n):
        b=bin(n)[2:]
        b = b.zfill(32)
        b = b[::-1]
        return int(b, 2)