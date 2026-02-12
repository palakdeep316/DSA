bool judgeCircle(char* moves) {
    int r=0,d=0;
        for (int i = 0; moves[i] != '\0'; i++){
            if (moves[i]=='L'){
                r++;
            }
            else if (moves[i]=='R')
                r--;
            else if (moves[i]=='U')
                d++;
            else if (moves[i]=='D')
                d--;
        }
        return (r==0 && d==0);
}