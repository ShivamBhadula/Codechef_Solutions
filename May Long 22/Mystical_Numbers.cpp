#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    ll test;
    cin>>test;
    while(test--)
    {
        ll n;
        cin>>n;
        int a[n];
        for(ll i=0;i<n;i++)
        cin>>a[i];
        ll dp[n+1][33];
        for(ll i=1;i<=n;i++)
        {
            ll temp=a[i-1];
            for(ll j=0;j<33;j++)
            {
                dp[i][j]=dp[i-1][j];
            }
            ll p=32;
            if(temp!=0)
            {
                p=(int)(log(temp)/log(2));
            }
            dp[i][p]++;
        }
        ll q;
        cin>>q;
        while(q--)
        {
            ll l ,r,x;
            ll p=32;
            ll count=0;
            cin>>l>>r>>x;
            if(x!=0)
            p=(int)(log(x)/log(2));
            count=dp[r][p]-dp[l-1][p];
            ll ans=(r-l+1)-count;
            cout<<ans<<endl;
        }
    }
    return 0;
}