class Solution(object):
    def replaceWords(self, dictionary, sentence):
        words=sentence.split()
        ans=[]
        for word in words:
            short=word
            for root in dictionary:
                if word.startswith(root):
                    if len(root)<len(short):
                        short=root
            ans.append(short)
        return " ".join(ans)
