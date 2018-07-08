/* mbinary
#########################################################################
# File : segTree.cc
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.coding.me
# Github: https://github.com/mbinary
# Created Time: 2018-05-19  23:06
# Description:
#########################################################################
*/

#include<stdio.h>
template<class type>
bool operator <(type x,type y){return x<y;}
template<class type>
class segTree
{
    int size;
    type *p;
public:
    segTree(int n=1);
    ~segTree();
    void update(int i,type x);
    type getMin(int a,int b){return find(a,b,1,size,1);}
    type find(int a,int b,int i,int j,int);
};
template<class type >
segTree<type>::segTree(int n):size(1)
{
    while(size<n)size*=2;
    p = new type[2*size-1];
    for (int i=0;i<2*size-1 ;++i )p[i]=MAX;
}
template<class type >
segTree<type>::~segTree(){delete p;}
template<class type>
void segTree<type>::update(int i,type x)
{
    i+=size-1;
    p[i]=x;
    while(i!=0){
        i/=2;
        p[i]=p[i*2]<p[i*2+1]?p[i*2]:p[i*2+1];
    }
}
template<class type>
type segTree<type>::find(int a,int b,int i , int j,int k)
{
    if(b<i}}j<a)return MAX;// to implement
    if (a<=i&&j<=b)return p[k];
    type l= find(a,b,i,(i+j)/2,2*k);
    type r= find(a,b,(i+j)/2+1,j,2*k+1);
    return l>r ?l:r;
}
