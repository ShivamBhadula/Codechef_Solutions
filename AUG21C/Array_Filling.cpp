

#include <bits/stdc++.h>
#include <bits/stdc++.h>
using namespace std;
#define ll  long long int

int main()
{
    
    int t;
    cin>>t;
    vector<pair<int,int>> l;
    
    while(t>0)
    {
        t--;
        ll n,m;
        cin>>n>>m;
        
        for(int i=0;i<m;i++)
        {
            ll x,y;
            cin>>x>>y;
            l.push_back({x,y});
        }
        sort(l.begin(),l.end(),greater<pair<int,int>>());

        ll lcm =1;
        ll sum=0;
        ll rem=n;
        for (int i=0;i<m && rem>0;i++)
        {
            ll a=l[i].first;
            ll b=l[i].second;
            lcm=(lcm*b)/(__gcd(lcm,b));
            sum=sum+(rem-n/lcm)*a;
            rem=n/lcm;
        }
        cout<<sum<<endl;
        l.clear();
    }
    return 0;
}
