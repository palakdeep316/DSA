class Solution(object):
    def letterCasePermutation(self, s):
        res = []
        def backtrack(i, path):
            if i == len(s):
                res.append(path)
                return
            if s[i].isdigit():
                backtrack(i + 1, path + s[i])
            else:
                backtrack(i + 1, path + s[i].lower())
                backtrack(i + 1, path + s[i].upper())
        backtrack(0, "")
        return res

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        s = sys.argv[1]
    else:
        try:
            s = input("Enter string: ").strip()
        except EOFError:
            sys.exit(1)

    for p in Solution().letterCasePermutation(s):
        print(p)