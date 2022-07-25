#include<bits/stdc++.h>
#define ll long long
#define f(i,n) for(int i=0;i<n;i++)
#define r(i,n) for(int i=n-1;i>0;i--)
using namespace std;

void solve()
{
    int a,b,n;
    cin>>a>>b>>n;
    if(a%b==0)
    {
        cout<<-1<<endl;
        return ;
    }
    int val=0;
    if(n%a==0)
    {
            val=n;
    }
    else
    {
        val=n+a-(n%a);
    }
    // cout<<val<<endl;
    if(val%a==0 && val%b!=0)
    {
        cout<<val<<endl;
    }
    else
    {
        cout<<val+a<<endl;
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