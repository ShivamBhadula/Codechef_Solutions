#include<bits/stdc++.h>
#define ll long long
#define f(i,n) for(int i=0;i<n;i++)
using namespace std;

int solve(ll a,ll b)
{
    return a*10+b*90;
}

int main()
{
    ll testcases;
    cin>>testcases;
    while(testcases--)
    {
        ll a;
        ll b;
        cin>>a>>b;
        cout<<solve(a,b)<<endl;
    }
    return 0;
}