#include<bits/stdc++.h>
#define ll long long 
using namespace std;
int main()
{
    ll t;
    cin>>t;
    while(t--)
    {
        ll a ,b,c,d;
        cin>>a>>b;
        cin>>c>>d;
        if(c>=a && d>=b)
        cout<<"POSSIBLE"<<endl;
        else
        cout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}