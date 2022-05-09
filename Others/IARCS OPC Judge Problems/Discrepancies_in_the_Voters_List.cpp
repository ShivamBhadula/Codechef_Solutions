#include <bits/stdc++.h>
using namespace std;
#define pi (3.141592653589)
#define mod 1000000007
#define int long long int
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
   int n1,n2,n3;
   cin>>n1>>n2>>n3;
   map<int,int> mp;
   int t=n1+n2+n3;
   while(t--)
   {
       int val;
       cin>>val;
       mp[val]++;
   }
   int count=0;
   for(auto i:mp)
   {
       if (i.ss>1)
       {
           count++;
       }
   }
   cout<<count<<endl;
   for(auto i:mp)
   {
       if (i.ss>1)
       {
           cout<<i.ff<<endl;
       }
   }
   return 0;
}
