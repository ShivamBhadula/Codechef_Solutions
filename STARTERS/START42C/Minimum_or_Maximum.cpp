#include<bits/stdc++.h>
#define ll long long
#define f(i,n) for(int i=0;i<n;i++)
#define r(i,n) for(int i=n-1;i>0;i--)
using namespace std;

void solve()
{
    ll n;
    cin>>n;
    ll a[n];
    f(i,n) cin>>a[i];
    ll maximum=a[0];
    ll minimum=a[0];
    for(ll i=0;i<n;i++)
    {
        maximum=max(a[i],maximum);
        minimum=min(a[i],minimum);
        if(a[i]!=maximum and a[i]!=minimum)
        {
            cout<<"NO"<<endl;
            return ;
        }
    }
    cout<<"YES"<<endl;
}

int main()
{
    ll testcases;
    cin>>testcases;
    while(testcases--)
    {
        solve();
    }
    return 0;
}