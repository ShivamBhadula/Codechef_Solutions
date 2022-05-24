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
    f(i,n)
    {
        cin>>a[i];
    }

    ll binary[32]={0};
    f(i,n)
    {
        ll bit=0;
        while(a[i])
        {
            if (binary[bit]==0)
            {
                binary[bit]=a[i]%2;
            }
            a[i]=int(a[i]/2);
            bit++;
        }
    }
    ll ans=0;
    f(i,32)
    {
        if(binary[i]==1)
        {
            ans++;
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