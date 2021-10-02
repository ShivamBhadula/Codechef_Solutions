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
   int t;
   cin>>t;
   while(t--)
   {
      int n,k;
      cin>>n>>k;
      int arr[n];
      for(int i=0;i<n;i++)
      {
          cin>>arr[i];
      }
      sort(arr, arr + n, greater<int>());
      int val=arr[k-1];
      int teams=0;
      for(int i=0;i<n;i++)
      {
          if(arr[i]<val)
          {
              break;
          }
          teams++;
      }
      cout<<teams<<endl;
   }
   return 0;
}
