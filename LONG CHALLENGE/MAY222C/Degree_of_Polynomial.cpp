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
   ll ans=0;
   r(i,n)
   {
       if(a[i]!=0)
       {
           ans=i;
           break;
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