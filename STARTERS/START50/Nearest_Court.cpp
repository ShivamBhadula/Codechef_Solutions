#include<bits/stdc++.h>
#define ll long long
#define f(i,n) for(int i=0;i<n;i++)
#define r(i,n) for(int i=n-1;i>0;i--)
using namespace std;

void solve()
{
    ll a,b;
    cin>>a>>b;
    ll ans=abs(a-b)/2;
    if (abs(a-b)%2==0)
    {
        cout<<ans<<endl;
    }
    else
    {
        cout<<ans+1<<endl;
    }
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