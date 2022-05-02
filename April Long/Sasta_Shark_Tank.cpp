#include<iostream>
#define ll long long
using namespace std;
int main()
{
    ll t;
    cin>>t;
    while(t--)
    {
        ll a,b;
        cin>>a>>b;
        if(a*10==b*5)
        cout<<"ANY"<<endl;
        else if(a*10>b*5)
        cout<<"FIRST"<<endl;
        else
        cout<<"SECOND"<<endl;
    }
    return 0;
}