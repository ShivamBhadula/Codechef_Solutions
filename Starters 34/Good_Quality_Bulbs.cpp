#include<bits/stdc++.h>
#define  ll long long
using namespace std;
int main()
{
    ll t;
    cin>>t;
    while(t--)
    {
        ll n,x;
        cin>>n>>x;
        ll sum=0;
        for(ll i=0;i<n-1;i++)
        {
            ll a;
            cin>>a;
            sum+=a;
        }
        if(n*x-sum<0)
        cout<<0<<endl;
        else
        cout<<n*x-sum<<endl;

    }
    return 0;
}