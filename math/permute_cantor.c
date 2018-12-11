#include<stdio.h>

//使用康托展开计算全排列, 下面存储的是0!,1!,2!...(n-1)!
long long int fac[100]={};
void calFac(int n)
{
    int i;
    fac[0]=1;
    for(i=1;i<=n;i++){
        fac[i]=i*fac[i-1];
    }
}

void permute(int *arr,int n,int sum)
{
    /*sum表示全排列由小到大排序后的名次,从0 开始计数, 由名次求出 n位的排列存储到 arr 中*/
    int i,j,ct=0,k, ct2;
    int flag[n];
    for(i=0;i<n;i++)flag[i]=1;

    for(i=n-1;i>=0;i--){
        for(j=i;j>=0;j--){
            if(j*fac[i]<=sum){
                ct2=0;
                for(k=0;k<n;++k){
                    //printf("i%d  j%d  k%d\n",i,j,k);
                    if(flag[k]==1)ct2++;
                    if(ct2>j)break;
                }
                arr[ct++] = k;
                flag[k]=0;
                sum -=j*fac[i];
                break;
            }
        }
    }
}

void printArr(int *p,int n)
{
    for(int i=0;i<n;++i)printf("%d, ",p[i]);
    printf("\n");
}

int main()
{
    int n = 5,arr[n];
    calFac(n);
    for(int i=0;i<5;++i)arr[i]=i; 
    for(int i=0;i<fac[n];++i){
        printArr(arr,n);
        permute(arr,n,i);
    }
    return 0;
}
        
