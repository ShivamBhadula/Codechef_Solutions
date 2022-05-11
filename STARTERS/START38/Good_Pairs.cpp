#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    ll test;
    cin>>test;
    while(test--)
    {
        ll l;
        cin>>l;
        ll a[l];
        ll b[l];

        for(ll i=0;i<l;i++)
        cin>>a[i];
        for(ll i=0;i<l;i++)
        cin>>b[i];

        map<pair<ll,ll>,ll> mp;
        ll ans=0;
        for(ll i=0;i<l;i++)
        {
            ans+=mp[{a[i],b[i]}];
            mp[{b[i],a[i]}]++;
        }
        cout<<ans<<endl;


    }
    return 0;
}