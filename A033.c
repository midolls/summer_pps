#include <stdio.h>
 
int main() {
    int n;
    int max = 0;
    int maxidx = 0;
    
    for (int i =0 ; i<5 ; i++){
        int sum =0;
        for (int j=0; j<4 ; j++){
            scanf("%d", &n);
            sum +=n;
            
            if(sum > max){
                max = sum;
                maxidx = i+1;
            }
        }
    }
    printf("%d %d",maxidx,max);
}