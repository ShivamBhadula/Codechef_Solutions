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
#define rfo(i, n) for(int i=n-1;i>=0;i--)
#define fo(i,n) for(int i=0;i<n;i++)
#define fast ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);


ll decimalToBinary(ll N)
{
    ll B_Number = 0;
    int cnt = 0;
    while (N != 0) {
        int rem = N % 2;
        ll c = pow(10, cnt);
        B_Number += rem * c;
        N /= 2;
        cnt++;
    }
    return B_Number;
}

ll reverseDigits(ll num)
{
    
    ll rev_num = 0;
    while (num > 0) {
        rev_num = rev_num * 10 + num % 10;
        num = num / 10;
    }
    return rev_num;
}

int isPalindrome(int num)
{
    ll n = decimalToBinary(num);
    ll rev_n = reverseDigits(n); 
    if (rev_n == n)
        return 1;
    else
    return 0;
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
      vector<int> ans;
      while (n>0)
      {
          for(int i=n;i>0;i--)
          {
              if(isPalindrome(i))
              {
                  ans.pb(i);
                  n=n-i;
                  break;
              }
          }
      }
   
   cout<<ans.size()<<endl;
   for(auto i:ans)
   cout<<i<<" ";
   cout<<endl;
   }
   return 0;
}
