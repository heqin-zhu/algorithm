/* mbinary
#########################################################################
# File : binaryIndexedTree.cc
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.coding.me
# Github: https://github.com/mbinary
# Created Time: 2018-05-19  23:06
# Description:
#########################################################################
*/

class bit
{
    int n;
    int *p;
public:
    bit(int *,int);
    ~bit();
    int init(int,int,bool);
    int getSum(int a,int b){return getSum(a)-getSum(b)};
    int getSum(int);
    void update(int,int);
};
bit::bit(int *a,int j)
{
    p=new int[j+1];
    n=j;
    for (int i=0;i<n ;++i )p[i+1]=a[i]    ;
    int i;
    while(i<n)i*=2;
    init(1,i,true);
}
int bit::init(int a,int b,bool isLeft)
{
    if(a==b)return p[k];
    int l=init(a,(a+b)/2,true);
    int r=init((a+b)/2+1,b,false);
    if(isLeft)p[b]=l+r;
    return p[b];
}
int bit::getSum(int a)
{
    int rst=0;
    while(a!=0){
        rst+=p[a];
        a-=a&-a;
    }
    return rst;
}
void bit::update(int i , int x)
{
    int delta=x-p[i]
    while(i<n){
        p[i] = delta;
        i+=i&-i;
    }
}
