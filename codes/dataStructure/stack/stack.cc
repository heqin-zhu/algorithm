#include<malloc.h>
#include<stdio.h>
#include<vector>
#define SZ 50
using namespace std;
template<typename type>
class stack
{
    int capacity;
    type *bottom,*top;
  public:
    stack(int n = SZ);
    stack( stack &);
    stack(int,type);
    stack(vector<type> &);
    type pop();
    int cp();
    void push(type);
    bool empty();
    type getTop();
};
template<typename type>
stack<type>::stack(int n):capacity(n)
{
    bottom = new type[capacity+1];
    top = bottom;
}

template<typename type>
stack<type>::stack(int n,type x):capacity(n*2)
{
    bottom = new type[capacity+1];
    top = bottom;
    for(int i = 0;i<n;++i)*(++top) = x;
}
template<typename type>
stack<type>::stack(vector<type> &vc):capacity (vc.size()*2)
{
    bottom = new type[capacity+1];
    top = bottom;
    for(int i = 0;i!=vc.size();++i){
        push(vc[i]);
    }
}
template<typename type>
stack<type>::stack(stack &s):capacity(s.capacity)
{
    bottom = new type[capacity+1];
    top = bottom;
    for(type *p= s.bottom;p!=s.top;)*(++top) = *(++p);
}
template<typename type>
int stack<type>::cp()
{
    return capacity;
}
template<typename type>
bool stack<type>::empty()
{
    return bottom == top;
}
template<typename type>
type stack<type>::getTop()
{
    return *top;
}
template<typename type>
type stack<type>::pop()
{
    if(bottom == top){
        printf("the stack is empty now\n");
        return 0;
    }else{
        return *(top--);
    }
}
template<typename type>
void stack<type>::push(type x)
{
    if(capacity == top-bottom){
        bottom = (type *)realloc(bottom,sizeof(type)*(2*capacity+1));
        top = bottom+capacity;
    }
    *(++top) = x;
}
int main()
{
    stack<char> sc(5,'z'),scc(sc);
    printf("stack copy\n");
    while(!scc.empty()){
        printf("%c\n",scc.pop());
    }
    vector<double> vc(50,2.3);
    stack<double> sd(vc);
    sd.push(3.4);
    printf("gettop%lf\n",sd.getTop());
    printf("vec copy\n");
    while(!sd.empty()){
        printf("%lf\n",sd.pop());
    }
    printf("empty %d\ncapacity%d",sd.empty(),sd.cp());
    return 0;
}
