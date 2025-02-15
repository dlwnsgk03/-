#include <stdio.h>

int x = 3, y = 3, count = 0, check = 3;

int star(int array, char picture[array][array+1], int currentX, int currentY){
    if(check > array-1){
        return 0;
    }
    else{
        if(currentX <= array-1 && currentY <= array-1){
            count++;
            int startY = currentY - check*2/3 + 1, endY = currentY - check/3 + 1;
            int startX = currentX - check*2/3 + 1, endX = currentX - check/3 + 1;
            int temp = startX;
            while(startY < endY){
                while(startX < endX){
                    picture[startY][startX] = ' ';
                    startX++;
                }
                startX=temp;
                startY++;
            }
            if(currentX == array-1){
                return star(array,picture,check,currentY+check);
            }
            else{
                return star(array,picture,currentX+check, currentY);
            }
        }
        else{
            check *= 3;
            return star(array,picture,check,check);
        }
    }
}

int main(){

    int N;
    scanf("%d",&N);
    int array = N+1;
    char picture[array][array+1];
    for(int i = 1; i <= array-1; i ++){
        for(int j = 1; j <= array-1; j++){
            picture[i][j] = '*';
        }
    }
    int start = 9;
    int blank = N^2/9;

    star(array, picture, 3, 3);
    for(int i = 1; i <= array-1; i++){
        for(int j = 1; j <= array-1; j++){
            printf("%c",picture[i][j]);
        }
        puts("");
    }

    return 0;
}