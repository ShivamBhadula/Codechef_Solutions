#include<bits/stdc++.h>
#define ll long long
#define f(i,n) for(int i=0;i<n;i++)
#define r(i,n) for(int i=n-1;i>0;i--)
ll n,x,arr[200001],dp[200001][2];
using namespace std;

void solve()
{
    cin >> n >> x;
        for(int i=1;i<=n;++i)
        cin >> arr[i];
        for(int i=2;i<=n;++i) 
        {
            dp[i][0]=max(dp[i-1][0]+(arr[i-1]^arr[i]),dp[i-1][1]+((arr[i-1]+x)^arr[i]));
            dp[i][1]=max(dp[i-1][0]+(arr[i-1]^(arr[i]+x)),dp[i-1][1]+((arr[i-1]+x)^(arr[i]+x)));
        }
        cout << max(dp[n][0],dp[n][1]) << endl;
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
