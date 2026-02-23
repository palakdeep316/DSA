class Solution(object):
    def recoverOrder(self, order, friends):
        s=[]
        for i in order:
            if i in friends:
                s.append(i)
        return s