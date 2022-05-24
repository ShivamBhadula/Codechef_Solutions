#include<bits/stdc++.h>
#define ll long long
#define f(i,n) for(int i=0;i<n;i++)
#define r(i,n) for(int i=n-1;i>0;i--)
using namespace std;

void solve()
{
    ll n;
    cin>>n;
    vector<vector<int>> val(n+1,vector<int>(1,-1));
    f(i,n)
    {
        ll temp;
        cin>>temp;
        val[temp].push_back(i);
    }
    ll ans=(ll)n*(n+1)/2;
    for(int i=1;i<=n;i++)
    {
        val[i].push_back(n);
        for(int j=1;j<(int)val[i].size();j++)
        {
            int l=val[i][j]-val[i][j-1]-1;
            ans-=l-i+1>0?l-i+1:0;
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