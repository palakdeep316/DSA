int mostWordsFound(char** sentences, int sentencesSize){
    int count=0;
    for (int i=0; i<sentencesSize;i++){
        int max=1;
        for (int j=0;sentences[i][j]!='\0';j++)
        {
            if (sentences[i][j]==' '){
                max++;
            }
        }
        if (max>=count){
            count=max;
        }
    }
    return count;
}