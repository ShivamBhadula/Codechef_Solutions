#include<bits/stdc++.h>
#define  ll long long
using namespace std;
int main()
{
    int test;
    cin>>test;
    while(test--)
    {
        ll n;
        cin>>n;
        unordered_map<int,int> mp;
        vector<int> a(n,0);
        for(ll i=0;i<n;i++)
        {
            cin>>a[i];
            mp[a[i]]++;
        }
        
        int ans=0;
        for(auto x:mp)
        {
            int val=x.first+x.second-1;
            ans=max(val,ans);
        }
        cout<<ans<<endl;
    }
    return 0;
}