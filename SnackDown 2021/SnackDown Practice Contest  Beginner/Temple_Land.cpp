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
   int t;
   cin>>t;
   while(t--)
   {
      int n;
      cin>>n;
      int arr[n];
      for(int i=0;i<n;i++)
      {
          cin>>arr[i];
      }
      if(n%2==0 or arr[0]!=1 || *max_element(arr,arr+n)!=int(n/2)+1)
      {
          cout<<"no"<<endl;
      }
      else
      {
          int len=0;
          for(int i=1;i<n;i++)
          {
              int val=abs(arr[i]-arr[i-1]);
              if(val!=1)
              {
                  break;
              }
              len++;
          }
          if(len==n-1)
          {
              cout<<"yes"<<endl;
          }
          else
          {
              cout<<"no"<<endl;
          }
      }
   }
   return 0;
}
