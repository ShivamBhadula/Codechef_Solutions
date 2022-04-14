#include<bits/stdc++.h>
#define  ll long long 
using namespace std;
int main()
{
    ll t;
    cin>>t;
    while(t--)
    {
        ll len;
        cin>>len;
        ll p=0,n=0;
        for(ll i=0;i<len;i++)
        {
            ll a;
            cin>>a;
            if(a>0)
            p++;
            else if(a<0)
            n++;
        }
        // cout<<p<<n<<endl;
        ll count=(p*(p-1))/2+(n*(n-1))/2;
        cout<<count<<endl;
    }
    return 0;
}