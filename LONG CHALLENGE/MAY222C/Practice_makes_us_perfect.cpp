#include<bits/stdc++.h>
#define ll long long
#define f(i,n) for(int i=0;i<n;i++)
using namespace std;

int solve(ll a[])
{
    ll ans=0;
    f(i,4)
    {
        if(a[i]>=10)
        {
            ans++;
        }
    }
    return ans;
}

int main()
{
    // ll testcases;
    // cin>>testcases;
    // while(testcases--)
    // {
        ll a[4];
        cin>>a[0]>>a[1]>>a[2]>>a[3]>>a[4];
        cout<<solve(a)<<endl;
    // }
    return 0;
}