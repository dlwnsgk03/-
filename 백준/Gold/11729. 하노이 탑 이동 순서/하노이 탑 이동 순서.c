#include <stdio.h>
#define INDEX 10000
int count = 1;

int hanoiTop(int N, int from, int temp, int to){
    if(N==1){
        printf("%d %d\n", from, to);
    }
    else{
        hanoiTop(N-1, from, to, temp);
        printf("%d %d\n", from,to);
        hanoiTop(N-1, temp, from, to);
    }
}

int main(){

    int N;
    scanf("%d",&N);
    int num = 1;
    for(int i = 0; i < N; i++){
        num *= 2;
    }
    printf("%d\n", num-1);
    hanoiTop(N,1,2,3);

    return 0;
}