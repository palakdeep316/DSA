int countDigits(int num) {
    int count=0;
    int n=num;
    while(num>0){
        int d=0;
        d=num%10;
        if(n%d==0){
            count+=1;
        }
        num/=10;
    }
    return count;
}