class Solution(object):
    def interpret(self, command):
        s=''
        i=0
        while(i<len(command)):
            if command[i]=='G':
                s+=command[i]
                i+=1
            elif command[i:i+2]=='()':
                s+='o'
                i+=2
            elif (command[i:i+4]=='(al)'):
                s+='al'
                i+=4
            else:
                continue
        return s