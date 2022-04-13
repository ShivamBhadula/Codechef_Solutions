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


void per(vector<int>v,int l,int r,vector<vector<int>>&p)
{
    if(l==r)
    p.push_back(v);
    else
    {
        for(int i=l;i<=r;i++)
        {
            swap(v[l],v[i]);
            per(v,l+1,r,p);
            swap(v[l],v[i]);
        }
    }
}
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        vector<int>v;
        ll fact=1;
        for(int i=1;i<=n;i++){    
        fact=fact*i;}
        vector<vector<int>>p;
        for(int i=1;i<=n;i++)
        {
            v.push_back(i);
        }
        ll expected_weight=0;
        per(v,0,v.size()-1,p);
        for(int i=0;i<p.size();i++)
        {
            ll weight=0;
            for(ll j=0;j<p[i].size();j++)
            {
                weight+=(j+1)*p[i][j];
            }
            expected_weight+=weight;
        }

        

    }
    return 0;
}
