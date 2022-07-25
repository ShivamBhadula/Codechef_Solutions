#include<bits/stdc++.h>
#define ll long long
#define f(i,n) for(int i=0;i<n;i++)
#define r(i,n) for(int i=n-1;i>0;i--)
using namespace std;

void solve()
{
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++)
    {
        int temp;
        cin>>temp;
        a[i]=temp;
    }
    int ans=0;
    int grp=0;
    for(int i=0;i<n;i++)
    {
        if(a[i]==1)
        {
            grp++;
        }
        else
        {
            ans+=(grp*(grp+1))/2;
            grp=0; 
        }
    }
    ans+=(grp*(grp+1))/2;
    cout<<ans<<endl;
}

int main()
{
    ll testcases;
    cin>>testcases;
    while(testcases--)
    {
        solve();
    }
    return 0;
}