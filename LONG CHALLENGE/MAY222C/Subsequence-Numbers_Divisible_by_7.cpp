#include<bits/stdc++.h>
#define ll long long
#define f(i,n) for(int i=0;i<n;i++)
#define r(i,n) for(int i=n-1;i>0;i--)
using namespace std;


void solve()
{
    ll n;
    cin>>n;
    ll mod=1e9+7;
    vector<int> arr(n,0);
    f(i,n) cin>>arr[i];
    
    vector<vector<int>> ans(n+1,vector<int>(7));
    ans[0][0]=1;
    f(i,n){
        ll l=(ll)to_string(arr[i]).size();
        ll power=1;
        while(l--) power*=10;
        f(j,7){
            ll temp=(j*power+arr[i])%7;
            ans[i+1][j]=(ans[i+1][j]+ans[i][j])%mod;
            ans[i+1][temp]=(ans[i+1][temp]+ans[i][j])%mod;
        }
    } 
    cout<<(ans[n][0]-1+ mod)%mod<<endl;
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