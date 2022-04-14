#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    ll t;
    cin>>t;
    while(t--)
    {
        ll n,x;
        cin>>n>>x;
        for(ll i=1;i<=n/2;i++)
        cout<<x-i<<" "<<x+i<<" ";
        if(n%2==1)
        cout<<x;
        cout<<endl;

    }
    return 0;
}