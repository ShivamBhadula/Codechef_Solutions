#include <bits/stdc++.h>
using namespace std;
#define pi (3.141592653589)
#define mod 1000000007
#define ll long long int
#define float double
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define all(c) c.begin(), c.end()
#define min3(a, b, c) min(c, min(a, b))
#define min4(a, b, c, d) min(d, min(c, min(a, b)))
#define max3(a,b,c) max(a,(max(b,c)))
#define rfo(i, n) for(int i=n-1;i>=0;i--)
#define fo(i,n) for(ll i=0;i<n;i++)
#define print cout<<
#define input cin>>
#define fast ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);


int32_t main()
{
   fast
   ll t=1;
   cin>>t;
   while(t--)
   {
      ll n,x,ans=0,opr=0;
      cin>>n>>x;
      unordered_map<int,int>mp1;
      unordered_map<int,int>mp2;
      fo(i,n)
      {
         ll z;
         input z;
         mp1[z]++;
         mp2[z]=1;
      }
      if (n==1)
      {
         print 1<<" "<<0<<endl;
         continue;
      }
      for(auto it:mp1)
      {
         if(it.ss==n)//if all elements are same
         {
            ans=n;
            break;
         }
         if(it.ss>=ans)//max-freq in original array
         {
            ans=it.ss;
         }
      }
      if(x==0)//A^0=A
      {
         print ans<<" "<<opr<<endl;
         continue;
      }
      for(auto it:mp1)
      {
         if(mp2[(it.ff)^x]==1)
         {
            if(it.ss+mp1[(it.ff)^x]>ans)
            {
               ans=it.ss+mp1[(it.ff)^x];
               opr=min(it.ss,mp1[(it.ff)^x]);
            }
            else if(it.ss+mp1[(it.ff)^x]==ans)
            {
               if(min(it.ss,mp1[(it.ff)^x])<opr)
               {
                  opr=min(it.ss,mp1[(it.ff)^x]);
               }
            }
         }
      }

      cout<<ans<<" "<<opr<<endl;
   }
   return 0;
}
