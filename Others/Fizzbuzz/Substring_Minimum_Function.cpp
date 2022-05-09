#include <bits/stdc++.h>
using namespace std;
#define pi (3.141592653589)
#define mod 1000000007
#define ll long long 
#define float double
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define all(c) c.begin(), c.end()
#define min3(a, b, c) min(c, min(a, b))
#define min4(a, b, c, d) min(d, min(c, min(a, b)))
#define rfo(i, n) for(int i=n-1;i>=0;i--)
#define fo(i,n) for(int i=0;i<n;i++)
#define fast ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);


int32_t main()
{
   fast
   int t;
   cin>>t;
   while(t--)
   {
    ll n,m,sum,x,z,y,cnt=0;
    cin>>n>>m;
    x=n-m;
    if(x<=m+1)
    cout<<x;
    else
    {
        y=x/(m+1);
        z=(x)%(m+1);
        ll cnty=(m+1)-z;
        ll cntx=y+1;
        sum=cnty * (y) * (y+1) /2 + z * (y+1) * (y+2) / 2;
        cout<<sum; 
    }
    cout<<endl;
   }
   return 0;
}
