#include <bits/stdc++.h>
using namespace std;
class Test
{
   public:
   void solve()
   {
     int q,n,l,r,enterInt,sum,min,sum2;
     cin>>q;
     for(int i=0;i<q;i++)
     {
        cin>>n>>l>>r;
        if(n>=l && n<=r)
        {
          cout<<n<<endl;
          continue;  
        }
        if(n<l)
        {
          cout<<l<<endl;
          continue;
        }
        sum2=INT_MAX;
        min=0;
     
        while(l<r && n/r<r)
        {
          int temp1=n/r,temp2=n%r;
          if(sum2>temp1+temp2)
          {
            sum2=temp1+temp2;
            min=r;
          }
        r=n/(temp1+1);
        }
        while(l<=r)
        {
          enterInt=n;
          sum=0;
          for(;;)
          {
            if(enterInt<l)
            {
              sum+=enterInt;
              if(sum<sum2)
              {
                min=l;
                sum2=sum;
              }
              break;   
            }
            sum+=enterInt%l;
            enterInt/=l;
            if(sum>=sum2)
              break;    
        }
        l++;
        }
      cout<<min<<endl;
      }
   }
};


int main()
{
  ios::sync_with_stdio(0);
  cin.tie(0);cout.tie(0);
  Test tt;
  tt.solve();
  return 0;
}
