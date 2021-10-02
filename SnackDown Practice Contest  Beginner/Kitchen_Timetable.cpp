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

int students(int a[],int b[],int n)
{
    int total=0;
     a[0]=0;
    for(int i=1;i<=n;i++)
    {
        int val=a[i]-a[i-1];
        if(val>=b[i])
        {
            total++;

        }
    }
    return total;
}

int32_t main()
{
   fast
   int t;
   cin>>t;
   while(t--)
   {
      int n;
      cin>>n;
      int time[n];
      int need[n];
      for(int i=1;i<=n;i++)
      {
          cin>>time[i];
      }
      for(int i=1;i<=n;i++)
      {
          cin>>need[i];
      }
      cout<<students(time,need,n)<<endl;
   }
   return 0;
}
