#include<bits/stdc++.h>
#define ll long long
#define f(i,n) for(int i=0;i<n;i++)
#define r(i,n) for(int i=n-1;i>0;i--)
using namespace std;

void solve()
{
    int x,y,n,r;
    cin>>x>>y>>n>>r;
    int pb=r/y;
    int nb=r/x;
    if(pb>=n)
    {
        cout<<0<<" "<<n<<endl;
        return ;
    }
    if(nb<x)
    {
        cout<<-1<<endl;
        return ;
    }
    pb=y*n; 
    int d=x-y;
    nb=(r-pb)/d;
    if((r-pb)%d!=0)
    {
        nb++;
    }
    cout<<nb<<" "<<n-nb<<endl;
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