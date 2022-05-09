#include <bits/stdc++.h>
using namespace std;
#define pi (3.141592653589)
#define mod 1000000007
//#define int long long int
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
   int n,m;
   cin>>n>>m;
   int t=n+m;
   vector<int> vi;
   vector<int>::iterator it;
   vector<int>::iterator ind;
   while(t--)
   {
      int val;
      cin>>val;
      if (val!=-1)
      {
          vi.pb(val);
      }
      else
      {
          int value=*max_element(vi.begin(),vi.end());
          cout<<value<<endl;;
          it=find(vi.begin(),vi.end(),value);
          ind=vi.erase(it);
      }
   }
   return 0;
}
