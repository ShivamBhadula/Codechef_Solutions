#include<bits/stdc++.h>
#define ll long long
#define f(i,n) for(int i=0;i<n;i++)
#define r(i,n) for(int i=n-1;i>0;i--)
using namespace std;

void solve()
{
    ll n,x;
    cin>>n>>x;
    if (n==1 and x==1)
    {
        cout<<1<<endl;
    }
    else if (x<n)
    {
        cout<<-1<<endl;
    }
    else
    {
        cout<<(x-n)+1<<" ";
        for(int i=1;i<=n;i++)
        {
            if(i!=x-n+1)
            {
                cout<<i<<" ";
            }
        }

        
        
        cout<<endl;
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