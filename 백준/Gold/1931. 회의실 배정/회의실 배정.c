#include <stdio.h>
int sorted[100000][2];

void merge(int I[][2], int start, int mid, int end){
    int s = start, e = mid+1, sortedIndex = start;

    while(s <= mid && e <= end){
        if(I[s][1] < I[e][1]){
            sorted[sortedIndex][0] = I[s][0];
            sorted[sortedIndex++][1] = I[s++][1];
        }
        else if(I[s][1] > I[e][1]){
            sorted[sortedIndex][0] = I[e][0];
            sorted[sortedIndex++][1] = I[e++][1];
        }
        else{
            if(I[s][0] < I[e][0]){
                sorted[sortedIndex][0] = I[s][0];
                sorted[sortedIndex++][1] = I[s++][1];
            }
            else{
                sorted[sortedIndex][0] = I[e][0];
                sorted[sortedIndex++][1] = I[e++][1];
            }
        }
    }

    if(s > mid){
        for(int i = e; i <= end; i++){
            sorted[sortedIndex][0] = I[i][0];
            sorted[sortedIndex++][1] = I[i][1];
        }
    }
    else{
        for(int i = s; i <= mid; i++){
            sorted[sortedIndex][0] = I[i][0];
            sorted[sortedIndex++][1] = I[i][1];
        }
    }

    for(int i = start; i <= end; i++){
        I[i][0] = sorted[i][0];
        I[i][1] = sorted[i][1];
    }
}

void mergeSort(int I[][2], int start, int end){
    int mid;
    if(start < end){
        mid = (start + end)/2;
        mergeSort(I, start, mid);
        mergeSort(I, mid+1, end);
        merge(I,start,mid,end);
    }
}

int main(){
    int N;
    scanf("%d", &N);

    int I[N][2];
    for(int i = 0; i < N; i++){
        scanf("%d %d", &I[i][0], &I[i][1]);
    }
    mergeSort(I,0,N-1);
    int endTime = I[0][1], count = 1;
    for(int i = 1; i < N; i++){
        if(endTime==I[i][0] || endTime < I[i][0]){
            endTime = I[i][1];
            count++;
        }
    }
    printf("%d\n", count);

    return 0;
}