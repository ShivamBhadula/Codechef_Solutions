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
      ll length,natural;
      cin>>length>>natural;
      vector<int> arr;
      vector<int> ans;
      for(ll i=0;i<length;i++){
          ll temp;
          cin>>temp;
          arr.pb(temp);
      }
      for(ll i=1;i<=natural;i++){
          vector<int> temp;
          for(ll j=0;j<length;j++){
              if(arr[j]!=i){
                  temp.pb(arr[j]);
              }
          }
          ll count=0;
          for(ll k=1;k<temp.size();k++){
              if(temp[k-1]!=temp[k]){
                  count++;
              }
          }
          ans.pb(count);
      }
      for(ll i=0;i<ans.size();i++){
          cout<<ans[i]<<" ";
      }
      cout<<endl;
   }
   return 0;
}
