#include <stdio.h>

int main(void){
    int mul =0;
    int n;
    int num[10];

    for(int i=0; i<10 ; i++) num[i]=0;

    for(int i=0;i<3;i++){
        scanf("%d",&n);
        mul*=n;
    }
    
    for(int i=0;mul>0;i++){
        n = mul % 10;
        num[n] += 1;
        mul /= 10;
    }    

    for(int j = 0; j<10; j++) printf("%d\n", num[j]);
}