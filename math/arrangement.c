#include<stdio.h>

void swap(int*arr,int i,int j)
{
    int tmp;
    tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
}
void nextArrangement(int *arr,int n)
{
    if(arr[n-1]>arr[n-2]){
        swap(arr,n-1,n-2);
    }else{
        int i;
        for(i=n-1;i>0;--i){
            if(arr[i]>arr[i-1])break;
        }
        if(i==0){//reverse arrangement, n,n-1,...,1
            for(;i<n;++i)arr[i] = i;
            return ;
        }
        i=i-1;
        for(int j=n-1;j>i;j--){
            if(arr[j]>arr[i]){
                int tmp = arr[j]; 
                for(int k = j;k>i;--k)arr[k] = arr[k-1]; 
                arr[i] =tmp;  
                break;
            }
        }
    }
}

void printArr(int *arr,int n)
{
    for(int i=0;i<n;++i)printf("%d ",arr[i]);
    printf("\n");
}
int main()
{
    int n = 4;
    int a[n];
    for(int i=0;i<n;++i)a[i]=i;
    long long int fac=1;
    for(int i=2;i<=n;++i)fac*=i;
    for(int i=0;i<fac;++i){
        printf("rank %d :",i); 
        printArr(a,n);
        nextArrangement(a,n);
    }
}
