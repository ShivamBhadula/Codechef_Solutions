#include<bits/stdc++.h>
using namespace std;
int main()
{
    int test;
    cin>>test;
    cout<<fixed<<setprecision(8);
    while(test--)
    {
        int n;
        cin>>n;
        int a[n];
        long double tot =0,cur=0;
        for(int i=0;i<n;i++)
        {
            cin>>a[i];
            tot+=a[i];
        }
        sort(a,a+n);
        long double ans=tot/n;
        for(int i=n-1;i>=0;i--)
        {
            tot-=a[i];
            cur+=a[i];
            ans=max(ans,(cur+tot/i)/(n+1-i));
        }
        cout<<ans<<endl;
    }
    return 0;
}