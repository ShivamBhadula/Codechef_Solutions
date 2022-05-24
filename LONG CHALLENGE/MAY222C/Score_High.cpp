#include<bits/stdc++.h>
#define ll long long
#define f(i,n) for(int i=0;i<n;i++)
using namespace std;


void solve()
{
    ll n;
    cin>>n;
    ll a[4];
    ll ans=0;
    f(i,4)
    {
        cin>>a[i];
        if(a[i]>ans)
        {
            ans=a[i];
        }
    }
    cout<<ans<<endl;
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