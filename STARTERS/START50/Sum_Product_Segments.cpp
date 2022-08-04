#include<bits/stdc++.h>
#define ll long long
#define f(i,n) for(int i=0;i<n;i++)
#define r(i,n) for(int i=n-1;i>0;i--)
using namespace std;

vector<ll> f;
void factors(ll n)
{
    for(ll i=1;i<=sqrt(n);i++)
    {
        if(n%i==0)
        {
            if(n/i==i)
            {
                f.push_back(i);
            }
            else
            {
                f.push_back(i);
                f.push_back(n/i);
            }
        }
    }
    sort(f.begin(),f.end());
}

void solve()
{
    ll x,y;
    cin>>x>>y;
    factors(y);
    bool sp=false;
    pair<ll,ll> s,p;
    for(auto &i:f)
    {
        if(i<=y/i){
        p={i,y/i};
        s={x-(i-1),i-1};
        if (s.first<=s.second)
        {
            sp=true;
            break;
        }
        s={y/i+1,x-(y/i+1)};
        if(s.first<=s.second)
        {
            sp=true;
            break;
        }
        }
        else
        {
            break;
        }
    }
    if(sp==true)
    {
        cout<<s.first<<" "<<s.second<<endl;
        cout<<p.first<<" "<<p.second<<endl;
    }
    else
    {
        cout<<-1<<endl;
    }

}

int main()
{
    ll testcases;
    cin>>testcases;
    while(testcases--)
    {
        f.clear();
        solve();
    }
    return 0;
}