#include<iostream>
using namespace std;
int main()
{
    int test;
    cin>>test;
    while(test--)
    {
        int a, b;
        cin>>a>>b;
        if(a==1)
        {
            if(b%2==0)
            cout<<"Even"<<endl;
            else
            cout<<"Odd"<<endl;
        }
        else if(b%2==1)
        {
            if(a%2==0)
            cout<<"even"<<endl;
            else
            cout<<"odd"<<endl;
        }
        else
        {
            cout<<"Impossible"<<endl;
        }

    }
    return 0;
}