#include<bits/stdc++.h>
#define ll long long
#define f(i,n) for(int i=0;i<n;i++)
#define r(i,n) for(int i=n-1;i>0;i--)
char s[200002];
using namespace std;

void solve()
{
    ll n,m;
    ll count=0;
    cin>>n>>m;
    for(ll i=1;i<=n;i++)
    {
        cin>>s[i];
        if (s[i]=='1')
        count++;
    }
    if(count==0)
    {
        cout<<n*m<<endl;
        return ;
    }
    if(count*m%2==1)
    {
        cout<<0<<endl;
        return;
    }
    ll ans=0;
    if(m%2==0)
    {
        for(int i=1;i<=n;++i)
        {
            if(s[i]=='1') break;
            ans++;
        }
        for(int i=n;i>=1;--i)
        {
            if(s[i]=='1') break;
            ans++;
        }
        cout<<ans+1<<endl;
        return ;
    }
    ll res=0;
    for(int i=1;i<=n;++i)
    {
        if(s[i]=='1') res++;
        if(res==count/2) ans++;
    }
    cout <<ans<<endl;
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

