#include<iostream>
#include<cmath>
#define ll long long
using namespace std;
int main()
{
    ll t;
    cin>>t;
    while(t--)
    {
        ll x,y;
        cin>>x>>y;
        cout<<abs(y-x)<<endl;
    }
    return 0;
}