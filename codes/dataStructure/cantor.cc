#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    float f;
    while(cin.peek()!='E'){
        cin>>f;
        getchar();
        bool flag=true;
        for(int i=0;i<50&&(f-0.0000001)>0;++i){
            int t=3*f;
            f=3*f-t;
            cout<<f<<endl;
            if(t==1){
                cout<<"NON-MEMBER"<<endl;
                flag = false;
                break;
            }
        }
        if(flag)cout<<"MEMBER"<<endl;
    }

}
