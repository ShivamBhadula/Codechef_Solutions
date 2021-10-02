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
      int n;
      cin>>n;
      int arr[n][n];
      for(int i=0;i<n;i++)
      {
          for(int j=0;j<n;j++)
          {
              arr[i][j]=1;
          }
      }
      if (n==2)
      {
          for(int i=0;i<n;i++)
          {
              fo(j,n)
              {
                  cout<<-1<<" ";
              }
              cout<<endl;
          }
      }
      else
      {
          fo(i,n)
          {
              arr[i][i]=-1;
          }
          fo(i,n)
          {
              fo(j,n)
              {
                  cout<<arr[i][j]<<" ";
              }
              cout<<endl;
          }
      }
   }
   return 0;
}
