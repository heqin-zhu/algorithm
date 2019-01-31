/* mbinary
#########################################################################
# File : permute_next_permutation.c
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-11-17  14:31
# Description: support duplicate values. 
                eg  [1,1,5]  nextPermutation  [1,5,1]
#########################################################################
*/
#include<stdio.h>

void swap(int*arr,int i,int j)
{
    int tmp;
    tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
}
void reverse(int *arr,int i,int j)
{
    while (i<j)swap(arr,i++,j--);
}
void nextPermutation(int *arr,int n)
{
    if(n>1){
        int i;
        for(i=n-1;i>0;--i){
            if(arr[i]>arr[i-1])break;
        }
        i-=1;
        if(i>=0){
            for(int j=n-1;j>i;j--){
                if(arr[j]>arr[i]){
                    swap(arr,j,i);
                    break;
                }
            }
        }
        reverse(arr,i+1,n-1);
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
        nextPermutation(a,n);
    }
}
