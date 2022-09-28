#include<bits/stdc++.h>
#define ll long long
#define f(i,n) for(int i=0;i<n;i++)
#define r(i,n) for(int i=n-1;i>0;i--)
using namespace std;

void solve()
{
    ll n;
    cin>>n;

    vector<ll> vi(n);

    ll val=0;

    for(ll i=n-1;i>=0;i--)
    {
        cin>>vi[i];
        if(vi[i]%2==1)
        {
            val^=i;
        }
    }
    if (val==0)
    {
        cout<<"Cook"<<endl;
    }
    else
    {
        cout<<"Chef"<<endl;
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