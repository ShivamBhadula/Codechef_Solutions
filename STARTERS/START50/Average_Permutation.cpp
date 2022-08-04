#include<bits/stdc++.h>
#define ll long long
#define f(i,n) for(int i=0;i<n;i++)
#define r(i,n) for(int i=n-1;i>0;i--)
using namespace std;

void solve()
{
    ll n;
    cin>>n;
    cout<<n-1<<" ";
    if (n<=4)
    {
        for(int i=1;i<=n-2;i++)
        {
            cout<<i<<" ";
        }
    }
    else
    {
        cout<<n-2<<endl;
        for(int i=1;i<=n-4;i++)
        {
            cout<<i<<" ";
        }
        cout<<n-3<<" ";
    }
    cout<<n<<endl;
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